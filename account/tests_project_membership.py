import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from account.employee_models import EmployeeProfile, CurrentProjectPlan, CurrentProjectAssignment, CurrentProjectDailyUpdate
from account.models import Project, ProjectMembership


User = get_user_model()


class ProjectMembershipTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.admin = User.objects.create_user(
            username="admin_pm",
            email="admin_pm@example.com",
            phoneno="9000000010",
            password="pass1234",
        )
        self.admin.is_staff = True
        self.admin.save()

        self.emp_user = User.objects.create_user(
            username="emp_pm",
            email="emp_pm@example.com",
            phoneno="9000000011",
            password="pass1234",
        )
        self.employee = EmployeeProfile.objects.create(
            user=self.emp_user,
            employee_id="DI40001",
            phone="9000000011",
            designation="Dev",
            status="active",
        )

        self.project = Project.objects.create(title="Proj", description="D", status="planned")

    def test_employee_projects_includes_membership_project(self):
        ProjectMembership.objects.create(project=self.project, employee=self.employee, role="member", is_active=True)
        self.client.force_authenticate(user=self.emp_user)
        res = self.client.get("/api/employees/projects/")
        self.assertEqual(res.status_code, 200)
        items = res.json()
        self.assertTrue(any(p.get("id") == self.project.id for p in items))

    def test_current_project_plan_requires_role_for_write(self):
        ProjectMembership.objects.create(project=self.project, employee=self.employee, role="member", is_active=True)
        self.client.force_authenticate(user=self.admin)
        res0 = self.client.post(f"/api/private-projects/{self.project.id}/plan/", data={}, format="json")
        self.assertEqual(res0.status_code, 201)

        res_assign = self.client.post(
            f"/api/private-projects/{self.project.id}/plan/assignments/",
            data={"employee": self.employee.id, "designation": "Dev"},
            format="json",
        )
        self.assertEqual(res_assign.status_code, 201)

        self.client.force_authenticate(user=self.emp_user)
        res = self.client.get(f"/api/private-projects/{self.project.id}/plan/")
        self.assertEqual(res.status_code, 200)

        res2 = self.client.patch(
            f"/api/private-projects/{self.project.id}/plan/",
            data=json.dumps({"timeline": "t1"}),
            content_type="application/json",
        )
        self.assertEqual(res2.status_code, 403)

        m = ProjectMembership.objects.get(project=self.project, employee=self.employee)
        m.role = "lead"
        m.save(update_fields=["role", "updated_at"])
        res3 = self.client.patch(
            f"/api/private-projects/{self.project.id}/plan/",
            data=json.dumps({"timeline": "t2"}),
            content_type="application/json",
        )
        self.assertEqual(res3.status_code, 403)

    def test_membership_api_admin_can_create_and_employee_can_view_own(self):
        self.client.force_authenticate(user=self.admin)
        res = self.client.post(
            "/api/project-memberships/",
            data={"project": self.project.id, "employee": self.employee.id, "role": "member", "is_active": True},
            format="json",
        )
        self.assertEqual(res.status_code, 200)

        self.client.force_authenticate(user=self.emp_user)
        res2 = self.client.get(f"/api/project-memberships/?project={self.project.id}")
        self.assertEqual(res2.status_code, 200)
        items = res2.json()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].get("role"), "member")

    def test_employee_projects_includes_plan_assignment_project(self):
        plan = CurrentProjectPlan.objects.create(project=self.project, project_name="Proj")
        CurrentProjectAssignment.objects.create(plan=plan, employee=self.employee, designation="Dev")

        self.client.force_authenticate(user=self.emp_user)
        res = self.client.get("/api/employees/me/projects/")
        self.assertEqual(res.status_code, 200)
        items = res.json()
        self.assertTrue(any(p.get("id") == self.project.id for p in items))

    def test_private_project_detail_includes_plan_assignments_with_ids(self):
        plan = CurrentProjectPlan.objects.create(project=self.project, project_name="Proj")
        assignment = CurrentProjectAssignment.objects.create(plan=plan, employee=self.employee, designation="Dev")

        self.client.force_authenticate(user=self.emp_user)
        res = self.client.get(f"/api/private-projects/{self.project.id}/")
        self.assertEqual(res.status_code, 200)
        payload = res.json()
        self.assertIn("project", payload)
        self.assertIn("plan", payload)
        self.assertIsNotNone(payload.get("plan"))
        assignments = payload.get("plan", {}).get("assignments", [])
        self.assertTrue(any(a.get("id") == assignment.id for a in assignments))

    def test_private_projects_list_only_includes_plan_assigned_projects_for_employee(self):
        other = Project.objects.create(title="Other", description="D2", status="planned")
        ProjectMembership.objects.create(project=other, employee=self.employee, role="member", is_active=True)

        self.client.force_authenticate(user=self.emp_user)
        res0 = self.client.get("/api/private-projects/")
        self.assertEqual(res0.status_code, 200)
        items0 = res0.json()
        self.assertFalse(any(p.get("id") == other.id for p in items0))

        plan = CurrentProjectPlan.objects.create(project=other, project_name="Other")
        assignment = CurrentProjectAssignment.objects.create(plan=plan, employee=self.employee, designation="Dev")
        res1 = self.client.get("/api/private-projects/")
        self.assertEqual(res1.status_code, 200)
        items1 = res1.json()
        self.assertTrue(any(p.get("id") == other.id for p in items1))
        matched = next((p for p in items1 if p.get("id") == other.id), None)
        self.assertIsNotNone(matched)
        assignments = (matched.get("plan") or {}).get("assignments", [])
        self.assertTrue(any(a.get("id") == assignment.id for a in assignments))

    def test_employee_can_auth_with_jwt_header_prefix(self):
        plan = CurrentProjectPlan.objects.create(project=self.project, project_name="Proj")
        CurrentProjectAssignment.objects.create(plan=plan, employee=self.employee, designation="Dev")

        access = str(RefreshToken.for_user(self.emp_user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"JWT {access}")
        res = self.client.get("/api/private-projects/")
        self.assertEqual(res.status_code, 200)
        items = res.json()
        self.assertTrue(any(p.get("id") == self.project.id for p in items))

    def test_employee_can_post_daily_update_and_update_own_comment_only(self):
        plan = CurrentProjectPlan.objects.create(project=self.project, project_name="Proj")
        assignment = CurrentProjectAssignment.objects.create(plan=plan, employee=self.employee, designation="Dev")

        self.client.force_authenticate(user=self.emp_user)
        res1 = self.client.patch(
            f"/api/private-projects/{self.project.id}/plan/assignments/{assignment.id}/",
            data={"employee_comment": "my update", "admin_comment": "nope"},
            format="json",
        )
        self.assertEqual(res1.status_code, 200)
        payload1 = res1.json()
        self.assertEqual(payload1.get("employee_comment"), "my update")
        self.assertNotEqual(payload1.get("admin_comment"), "nope")

        res2 = self.client.post(
            f"/api/private-projects/{self.project.id}/plan/assignments/{assignment.id}/daily-updates/",
            data={"date": "2026-03-01", "text": "done"},
            format="json",
        )
        self.assertEqual(res2.status_code, 201)
        self.assertEqual(CurrentProjectDailyUpdate.objects.filter(assignment=assignment).count(), 1)
