from django.db.models import Q
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.authentication import CookieJWTAuthentication, QuietJWTAuthentication
from account.employee_models import CurrentProjectDailyUpdate, EmployeeTicket
from account.models import Project
from account.serializers import ProjectListSerializer


def _is_admin(user):
    return bool(
        user
        and getattr(user, "is_authenticated", False)
        and (getattr(user, "is_staff", False) or getattr(user, "is_superuser", False) or getattr(user, "is_admin", False))
    )


class DashboardSummaryAPI(APIView):
    authentication_classes = [CookieJWTAuthentication, QuietJWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = getattr(request, "user", None)
        employee = getattr(user, "employee_profile", None)

        if _is_admin(user) or employee is None:
            projects_qs = Project.objects.all().order_by("-updated_at")
            tickets_qs = EmployeeTicket.objects.all().order_by("-updated_at")
            updates_qs = CurrentProjectDailyUpdate.objects.select_related("assignment", "assignment__plan", "assignment__plan__project").order_by("-created_at")
        else:
            projects_qs = (
                Project.objects.filter(Q(current_project_plan__assignments__employee=employee) | Q(private_project_plan__assignments__employee=employee))
                .distinct()
                .order_by("-updated_at")
            )
            tickets_qs = EmployeeTicket.objects.filter(Q(employee=employee) | Q(assigned_to=employee)).order_by("-updated_at")
            updates_qs = (
                CurrentProjectDailyUpdate.objects.select_related("assignment", "assignment__plan", "assignment__plan__project")
                .filter(assignment__employee=employee)
                .order_by("-created_at")
            )

        open_ticket_statuses = ["open", "in_progress"]
        tickets_open_count = tickets_qs.filter(status__in=open_ticket_statuses).count()

        recent_projects = projects_qs[:5]
        recent_tickets = tickets_qs[:5]
        recent_updates = updates_qs[:5]

        updates_payload = []
        for u in recent_updates:
            assignment = getattr(u, "assignment", None)
            plan = getattr(assignment, "plan", None) if assignment else None
            project = getattr(plan, "project", None) if plan else None
            updates_payload.append(
                {
                    "id": u.id,
                    "date": getattr(u, "date", None),
                    "text": getattr(u, "text", ""),
                    "created_at": getattr(u, "created_at", None),
                    "assignment_id": getattr(assignment, "id", None),
                    "project_id": getattr(project, "id", None),
                    "project_title": getattr(project, "title", None),
                }
            )

        ticket_payload = []
        for t in recent_tickets:
            ticket_payload.append(
                {
                    "id": t.id,
                    "ticket_number": getattr(t, "ticket_number", ""),
                    "title": getattr(t, "title", ""),
                    "status": getattr(t, "status", ""),
                    "priority": getattr(t, "priority", ""),
                    "updated_at": getattr(t, "updated_at", None),
                }
            )

        return Response(
            {
                "projects": {
                    "count": projects_qs.count(),
                    "recent": ProjectListSerializer(recent_projects, many=True, context={"request": request}).data,
                },
                "tickets": {
                    "count": tickets_qs.count(),
                    "open_count": tickets_open_count,
                    "recent": ticket_payload,
                },
                "updates": {
                    "count": updates_qs.count(),
                    "recent": updates_payload,
                },
            },
            status=status.HTTP_200_OK,
        )

