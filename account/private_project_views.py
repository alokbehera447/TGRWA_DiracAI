from django.utils import timezone
from django.db.models import Q
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.authentication import QuietJWTAuthentication, CookieJWTAuthentication
from account.employee_models import (
    CurrentProjectPlan,
    CurrentProjectAssignment,
    CurrentProjectDailyUpdate,
    PrivateProjectPlan,
    PrivateProjectAssignment,
    PrivateProjectDailyUpdate,
)
from account.employee_serializers import (
    CurrentProjectPlanSerializer,
    CurrentProjectAssignmentSerializer,
    CurrentProjectDailyUpdateSerializer,
    PrivateProjectPlanSerializer,
    PrivateProjectAssignmentSerializer,
    PrivateProjectDailyUpdateSerializer,
)
from account.models import Project
from account.pagination import DefaultPageNumberPagination, wants_pagination
from account.serializers import ProjectSerializer, ProjectListSerializer
from account.permissions import CanAccessPrivateProject


def _is_admin(user):
    return bool(
        user
        and getattr(user, "is_authenticated", False)
        and (getattr(user, "is_staff", False) or getattr(user, "is_superuser", False) or getattr(user, "is_admin", False))
    )


def _can_read_project(user, project):
    if not user or not getattr(user, "is_authenticated", False):
        return False
    if _is_admin(user):
        return True
    if getattr(project, "project_manager_id", None) == getattr(user, "id", None):
        return True
    employee = getattr(user, "employee_profile", None)
    if not employee:
        return False
    if getattr(employee, "private_project_id", None) == getattr(project, "id", None):
        return True
    try:
        current_plan = getattr(project, "current_project_plan", None)
        if current_plan and current_plan.assignments.filter(employee=employee).exists():
            return True
        private_plan = getattr(project, "private_project_plan", None)
        if private_plan and private_plan.assignments.filter(employee=employee).exists():
            return True
    except Exception:
        pass
    if project.employee_team_members.filter(pk=employee.pk).exists():
        return True
    membership = getattr(project, "memberships", None)
    if membership is None:
        return False
    m = membership.filter(employee=employee, is_active=True).first()
    if not m:
        return False
    return True


def _can_write_project(user, project):
    if not user or not getattr(user, "is_authenticated", False):
        return False
    if _is_admin(user):
        return True
    if getattr(project, "project_manager_id", None) == getattr(user, "id", None):
        return True
    employee = getattr(user, "employee_profile", None)
    if not employee:
        return False
    membership = getattr(project, "memberships", None)
    if membership is None:
        return False
    m = membership.filter(employee=employee, is_active=True).first()
    if not m:
        return False
    return getattr(m, "role", None) in {"pm", "lead"}


def _project_queryset_for_user(user):
    qs = Project.objects.select_related("project_manager").all()
    if not user or not getattr(user, "is_authenticated", False):
        return Project.objects.none()
    if _is_admin(user):
        return qs
    employee = getattr(user, "employee_profile", None)
    q = Q(project_manager=user)
    if employee:
        private_project_id = getattr(employee, "private_project_id", None)
        if private_project_id:
            q = q | Q(pk=private_project_id)
        q = q | Q(employee_team_members=employee) | Q(memberships__employee=employee, memberships__is_active=True)
        q = q | Q(current_project_plan__assignments__employee=employee) | Q(private_project_plan__assignments__employee=employee)
    return qs.filter(q).distinct()


class PrivateProjectsAPI(APIView):
    authentication_classes = [CookieJWTAuthentication, QuietJWTAuthentication, SessionAuthentication]
    permission_classes = [CanAccessPrivateProject]
    parser_classes = [JSONParser]

    def get_permissions(self):
        if getattr(self.request, "method", "").upper() == "OPTIONS":
            return [AllowAny()]
        return [CanAccessPrivateProject()]

    def get(self, request):
        qs = (
            _project_queryset_for_user(request.user)
            .select_related("current_project_plan", "private_project_plan")
            .prefetch_related(
                "current_project_plan__assignments",
                "current_project_plan__assignments__daily_updates",
                "current_project_plan__ticket_assignments",
                "private_project_plan__assignments",
                "private_project_plan__assignments__daily_updates",
            )
            .order_by("-updated_at")
        )
        employee = getattr(request.user, "employee_profile", None)
        if employee and not _is_admin(request.user):
            qs = qs.filter(
                Q(current_project_plan__assignments__employee=employee) | Q(private_project_plan__assignments__employee=employee)
            ).distinct()
        items = []
        summary = request.query_params.get("summary") in ("1", "true", "yes")
        full = request.query_params.get("full") in ("1", "true", "yes")
        for project in qs:
            payload = (ProjectSerializer(project, context={"request": request}).data if full else ProjectListSerializer(project, context={"request": request}).data)
            plan = getattr(project, "current_project_plan", None) or getattr(project, "private_project_plan", None)
            if isinstance(plan, CurrentProjectPlan):
                plan_data = CurrentProjectPlanSerializer(plan, context={"request": request}).data
                assigned_ids = [a.employee_id for a in getattr(plan, "assignments", []).all()]
                assigned_codes = [a.employee.employee_id for a in getattr(plan, "assignments", []).all() if getattr(a, "employee", None)]
                if summary and isinstance(plan_data, dict):
                    assignments = plan_data.pop("assignments", None)
                    plan_data.pop("employees", None)
                    ticket_assignments = plan_data.pop("ticket_assignments", None)
                    plan_data["assignments_count"] = len(assignments or []) if isinstance(assignments, list) else 0
                    plan_data["ticket_assignments_count"] = len(ticket_assignments or []) if isinstance(ticket_assignments, list) else 0
                payload["plan"] = plan_data
            else:
                plan_data = PrivateProjectPlanSerializer(plan, context={"request": request}).data if plan else None
                assigned_ids = [a.employee_id for a in getattr(plan, "assignments", []).all()] if plan else []
                assigned_codes = [a.employee.employee_id for a in getattr(plan, "assignments", []).all() if getattr(a, "employee", None)] if plan else []
                if summary and isinstance(plan_data, dict):
                    assignments = plan_data.pop("assignments", None)
                    plan_data.pop("employees", None)
                    plan_data["assignments_count"] = len(assignments or []) if isinstance(assignments, list) else 0
                payload["plan"] = plan_data
            payload["assigned_employee_ids"] = assigned_ids
            payload["assigned_employee_codes"] = assigned_codes
            if employee:
                payload["is_assigned_to_me"] = bool(employee.id in set(assigned_ids) or employee.employee_id in set(assigned_codes))
            items.append(payload)
        if wants_pagination(request):
            paginator = DefaultPageNumberPagination()
            page = paginator.paginate_queryset(items, request)
            return paginator.get_paginated_response(page)
        return Response(items, status=status.HTTP_200_OK)

    def post(self, request):
        if not _is_admin(request.user) and not getattr(request.user, "is_staff", False) and not getattr(request.user, "is_superuser", False):
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)

        payload = request.data if isinstance(request.data, dict) else {}
        plan_payload = payload.get("plan") if isinstance(payload.get("plan"), dict) else payload
        project_id = plan_payload.get("project") or plan_payload.get("project_id") or payload.get("project") or payload.get("project_id")
        if project_id in (None, "", "null"):
            return Response({"detail": "project_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            project = Project.objects.get(pk=int(str(project_id).strip()))
        except Exception:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        if not _can_write_project(request.user, project):
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)

        data = dict(plan_payload)
        data.pop("id", None)
        data.pop("project_id", None)
        data.setdefault("project", project.id)

        incoming_project_name = data.get("project_name")
        incoming_project_description = data.get("project_description")
        if incoming_project_name not in (None, "", "null"):
            project.title = incoming_project_name
        if incoming_project_description not in (None, "", "null"):
            project.description = incoming_project_description

        status_value = data.pop("status", None) or payload.get("status")
        if isinstance(status_value, str) and status_value.strip().lower() in {"planned", "ongoing", "completed"}:
            project.status = status_value.strip().lower()
        if "start_date" in data:
            project.start_date = data.get("start_date")
        if "end_date" in data:
            project.end_date = data.get("end_date")
        project.save(update_fields=["title", "description", "status", "start_date", "end_date", "updated_at"])

        plan = CurrentProjectPlan.objects.filter(project=project).first()
        if plan is None:
            plan = CurrentProjectPlan.objects.create(project=project)
        serializer = CurrentProjectPlanSerializer(plan, data=data, partial=True, context={"request": request})
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()

        project_payload = (
            ProjectSerializer(project, context={"request": request}).data
            if request.query_params.get("full") in ("1", "true", "yes")
            else ProjectListSerializer(project, context={"request": request}).data
        )
        response_payload = dict(project_payload)
        response_payload["project"] = project_payload
        response_payload["plan"] = CurrentProjectPlanSerializer(plan, context={"request": request}).data
        return Response(response_payload, status=status.HTTP_201_CREATED)


class PrivateProjectDetailAPI(APIView):
    authentication_classes = [CookieJWTAuthentication, QuietJWTAuthentication, SessionAuthentication]
    permission_classes = [CanAccessPrivateProject]
    parser_classes = [JSONParser]

    def get_permissions(self):
        if getattr(self.request, "method", "").upper() == "OPTIONS":
            return [AllowAny()]
        return [CanAccessPrivateProject()]

    def get(self, request, pk):
        project = (
            _project_queryset_for_user(request.user)
            .select_related("current_project_plan", "private_project_plan")
            .prefetch_related(
                "current_project_plan__assignments",
                "current_project_plan__assignments__daily_updates",
                "current_project_plan__ticket_assignments",
                "private_project_plan__assignments",
                "private_project_plan__assignments__daily_updates",
            )
            .filter(pk=pk)
            .first()
        )
        if project is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            self.check_object_permissions(request, project)
        except Exception:
            if not _is_admin(request.user):
                return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
            raise
        plan = getattr(project, "current_project_plan", None) or getattr(project, "private_project_plan", None)
        project_payload = (
            ProjectSerializer(project, context={"request": request}).data
            if request.query_params.get("full") in ("1", "true", "yes")
            else ProjectListSerializer(project, context={"request": request}).data
        )
        plan_payload = (
            CurrentProjectPlanSerializer(plan, context={"request": request}).data
            if isinstance(plan, CurrentProjectPlan)
            else (PrivateProjectPlanSerializer(plan, context={"request": request}).data if plan else None)
        )
        response_payload = dict(project_payload)
        response_payload["project"] = project_payload
        response_payload["plan"] = plan_payload
        if isinstance(plan_payload, dict):
            response_payload["project_name"] = plan_payload.get("project_name") or project_payload.get("title") or ""
            response_payload["project_description"] = plan_payload.get("project_description") or project_payload.get("description") or ""
            response_payload["timeline"] = plan_payload.get("timeline") or project_payload.get("timeline") or ""
            response_payload["start_date"] = plan_payload.get("start_date") if plan_payload.get("start_date") is not None else project_payload.get("start_date")
            response_payload["end_date"] = plan_payload.get("end_date") if plan_payload.get("end_date") is not None else project_payload.get("end_date")
        return Response(response_payload, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        return self._save_plan(request, pk, partial=True)

    def put(self, request, pk):
        return self._save_plan(request, pk, partial=False)

    def _save_plan(self, request, pk, partial):
        project = _project_queryset_for_user(request.user).filter(pk=pk).first()
        if project is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        if not _is_admin(request.user):
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)

        payload = request.data if isinstance(request.data, dict) else {}
        plan_payload = payload.get("plan") if isinstance(payload.get("plan"), dict) else payload
        data = dict(plan_payload) if isinstance(plan_payload, dict) else {}
        data.pop("id", None)
        data.pop("project_id", None)
        data.setdefault("project", project.id)

        incoming_project_name = data.get("project_name")
        incoming_project_description = data.get("project_description")
        if incoming_project_name not in (None, "", "null"):
            project.title = incoming_project_name
        if incoming_project_description not in (None, "", "null"):
            project.description = incoming_project_description

        status_value = data.pop("status", None) or payload.get("status")
        if isinstance(status_value, str) and status_value.strip().lower() in {"planned", "ongoing", "completed"}:
            project.status = status_value.strip().lower()
        if "start_date" in data:
            project.start_date = data.get("start_date")
        if "end_date" in data:
            project.end_date = data.get("end_date")
        project.save(update_fields=["title", "description", "status", "start_date", "end_date", "updated_at"])

        plan = CurrentProjectPlan.objects.filter(project=project).first()
        if plan is None:
            plan = CurrentProjectPlan.objects.create(project=project)
        serializer = CurrentProjectPlanSerializer(plan, data=data, partial=partial, context={"request": request})
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        plan = (
            CurrentProjectPlan.objects.select_related("project")
            .prefetch_related("assignments", "assignments__daily_updates", "ticket_assignments")
            .filter(pk=plan.pk)
            .first()
            or plan
        )

        project_payload = (
            ProjectSerializer(project, context={"request": request}).data
            if request.query_params.get("full") in ("1", "true", "yes")
            else ProjectListSerializer(project, context={"request": request}).data
        )
        response_payload = dict(project_payload)
        response_payload["project"] = project_payload
        plan_payload = CurrentProjectPlanSerializer(plan, context={"request": request}).data
        response_payload["plan"] = plan_payload
        if isinstance(plan_payload, dict):
            response_payload["project_name"] = plan_payload.get("project_name") or project_payload.get("title") or ""
            response_payload["project_description"] = plan_payload.get("project_description") or project_payload.get("description") or ""
            response_payload["timeline"] = plan_payload.get("timeline") or project_payload.get("timeline") or ""
            response_payload["start_date"] = plan_payload.get("start_date") if plan_payload.get("start_date") is not None else project_payload.get("start_date")
            response_payload["end_date"] = plan_payload.get("end_date") if plan_payload.get("end_date") is not None else project_payload.get("end_date")
        return Response(response_payload, status=status.HTTP_200_OK)


class PrivateProjectPlanAPI(APIView):
    authentication_classes = [CookieJWTAuthentication, QuietJWTAuthentication, SessionAuthentication]
    permission_classes = [CanAccessPrivateProject]
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def get_permissions(self):
        if getattr(self.request, "method", "").upper() == "OPTIONS":
            return [AllowAny()]
        return [CanAccessPrivateProject()]

    def get(self, request, pk):
        project = _project_queryset_for_user(request.user).filter(pk=pk).first()
        if project is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            self.check_object_permissions(request, project)
        except Exception:
            if not _is_admin(request.user):
                return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
            raise
        plan = CurrentProjectPlan.objects.filter(project=project).first()
        if plan is None:
            return Response({"detail": "Plan not created"}, status=status.HTTP_404_NOT_FOUND)
        return Response(CurrentProjectPlanSerializer(plan, context={"request": request}).data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        project = _project_queryset_for_user(request.user).filter(pk=pk).first()
        if project is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        if not _is_admin(request.user):
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        plan = CurrentProjectPlan.objects.filter(project=project).first()
        if plan is not None:
            return Response(CurrentProjectPlanSerializer(plan, context={"request": request}).data, status=status.HTTP_200_OK)
        plan = CurrentProjectPlan.objects.create(
            project=project,
            start_date=project.start_date,
            end_date=project.end_date,
            timeline=getattr(project, "timeline", "") or "",
            project_name=project.title,
            project_description=project.description or "",
        )
        return Response(CurrentProjectPlanSerializer(plan, context={"request": request}).data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        project = _project_queryset_for_user(request.user).filter(pk=pk).first()
        if project is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        if not _is_admin(request.user):
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        plan = CurrentProjectPlan.objects.filter(project=project).first()
        if plan is None:
            return Response({"detail": "Plan not created"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CurrentProjectPlanSerializer(plan, data=request.data, partial=True, context={"request": request})
        serializer.is_valid(raise_exception=True)
        plan = serializer.save()
        return Response(CurrentProjectPlanSerializer(plan, context={"request": request}).data, status=status.HTTP_200_OK)

class PrivateProjectPlanAssignmentsAPI(APIView):
    authentication_classes = [CookieJWTAuthentication, QuietJWTAuthentication, SessionAuthentication]
    permission_classes = [CanAccessPrivateProject]
    parser_classes = [JSONParser]

    def get_permissions(self):
        if getattr(self.request, "method", "").upper() == "OPTIONS":
            return [AllowAny()]
        return [CanAccessPrivateProject()]

    def post(self, request, pk):
        project = _project_queryset_for_user(request.user).filter(pk=pk).first()
        if project is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        if not _is_admin(request.user):
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        plan = CurrentProjectPlan.objects.filter(project=project).first()
        if plan is None:
            return Response({"detail": "Plan not created"}, status=status.HTTP_404_NOT_FOUND)

        payload = request.data if isinstance(request.data, dict) else {}
        employee_id = payload.get("employee")
        if employee_id in (None, "", "null"):
            return Response({"detail": "Invalid payload"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            employee_obj = getattr(request.user, "employee_profile", None)
            if employee_obj and str(employee_obj.id) == str(employee_id):
                employee_obj = employee_obj
            else:
                from account.employee_models import EmployeeProfile

                employee_obj = EmployeeProfile.objects.get(pk=int(str(employee_id).strip()))
        except Exception:
            return Response({"detail": "Invalid employee"}, status=status.HTTP_400_BAD_REQUEST)

        assignment, _ = CurrentProjectAssignment.objects.get_or_create(plan=plan, employee=employee_obj)
        if not assignment.designation:
            assignment.designation = getattr(employee_obj, "designation", "") or ""
        for f in ("designation", "start_date", "end_date", "work", "status", "admin_comment", "employee_comment"):
            if f in payload:
                setattr(assignment, f, payload.get(f))
        assignment.save()

        return Response(CurrentProjectAssignmentSerializer(assignment, context={"request": request}).data, status=status.HTTP_201_CREATED)


class PrivateProjectPlanAssignmentAPI(APIView):
    authentication_classes = [CookieJWTAuthentication, QuietJWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get_permissions(self):
        if getattr(self.request, "method", "").upper() == "OPTIONS":
            return [AllowAny()]
        return [IsAuthenticated()]

    def patch(self, request, pk, assignment_id):
        project = _project_queryset_for_user(request.user).filter(pk=pk).first()
        if project is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        plan = CurrentProjectPlan.objects.filter(project=project).first()
        if plan is None:
            return Response({"detail": "Plan not created"}, status=status.HTTP_404_NOT_FOUND)
        assignment = CurrentProjectAssignment.objects.filter(plan=plan, pk=assignment_id).first()
        if assignment is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        payload = request.data if isinstance(request.data, dict) else {}
        if not _is_admin(request.user):
            employee = getattr(getattr(request, "user", None), "employee_profile", None)
            if not employee or assignment.employee_id != getattr(employee, "id", None):
                return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
            allowed = {"employee_comment"}
            for k in list(payload.keys()):
                if k not in allowed:
                    payload.pop(k, None)

        for f in ("designation", "start_date", "end_date", "work", "status", "admin_comment", "employee_comment"):
            if f in payload:
                setattr(assignment, f, payload.get(f))
        assignment.save()
        return Response(CurrentProjectAssignmentSerializer(assignment, context={"request": request}).data, status=status.HTTP_200_OK)

    def delete(self, request, pk, assignment_id):
        project = _project_queryset_for_user(request.user).filter(pk=pk).first()
        if project is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        if not _is_admin(request.user):
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        plan = CurrentProjectPlan.objects.filter(project=project).first()
        if plan is None:
            return Response({"detail": "Plan not created"}, status=status.HTTP_404_NOT_FOUND)
        assignment = CurrentProjectAssignment.objects.filter(plan=plan, pk=assignment_id).first()
        if assignment is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PrivateProjectDailyUpdatesAPI(APIView):
    authentication_classes = [CookieJWTAuthentication, QuietJWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get_permissions(self):
        if getattr(self.request, "method", "").upper() == "OPTIONS":
            return [AllowAny()]
        return [IsAuthenticated()]

    def post(self, request, pk, assignment_id):
        project = _project_queryset_for_user(request.user).filter(pk=pk).first()
        if project is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        plan = CurrentProjectPlan.objects.filter(project=project).first()
        if plan is None:
            return Response({"detail": "Plan not created"}, status=status.HTTP_404_NOT_FOUND)
        assignment = CurrentProjectAssignment.objects.filter(plan=plan, pk=assignment_id).first()
        if assignment is None:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        if not _is_admin(request.user):
            employee = getattr(getattr(request, "user", None), "employee_profile", None)
            if not employee or assignment.employee_id != getattr(employee, "id", None):
                return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)

        payload = request.data if isinstance(request.data, dict) else {}
        text = (payload.get("text") or "").strip()
        date = payload.get("date")
        if not text or not date:
            return Response({"detail": "Invalid payload"}, status=status.HTTP_400_BAD_REQUEST)

        update = CurrentProjectDailyUpdate.objects.create(assignment=assignment, date=date, text=text)
        return Response(CurrentProjectDailyUpdateSerializer(update, context={"request": request}).data, status=status.HTTP_201_CREATED)
