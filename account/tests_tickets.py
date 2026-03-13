import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from account.employee_models import EmployeeProfile, EmployeeTicket, CurrentProjectPlan
from account.models import Project


User = get_user_model()


class EmployeeTicketsAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.admin = User.objects.create_user(
            username="admin_ticket",
            email="admin_ticket@example.com",
            phoneno="9000000003",
            password="pass1234",
        )
        self.admin.is_staff = True
        self.admin.save()

        self.emp_user = User.objects.create_user(
            username="emp_ticket",
            email="emp_ticket@example.com",
            phoneno="9000000004",
            password="pass1234",
        )
        self.employee = EmployeeProfile.objects.create(
            user=self.emp_user,
            employee_id="DI30001",
            phone="9000000004",
            designation="Dev",
            status="active",
        )

    def test_admin_can_create_ticket_and_employee_can_list(self):
        self.client.force_authenticate(user=self.admin)
        payload = {
            "employee": self.employee.id,
            "title": "Fix bug",
            "description": "Details",
            "priority": "high",
        }
        res = self.client.post("/api/employee-tickets/", data=payload, format="json")
        self.assertEqual(res.status_code, 201)
        ticket_id = res.json().get("id")
        self.assertTrue(ticket_id)

        self.client.force_authenticate(user=self.emp_user)
        res2 = self.client.get("/api/employee-tickets/")
        self.assertEqual(res2.status_code, 200)
        payload2 = res2.json()
        items = payload2.get("results", []) if isinstance(payload2, dict) else payload2
        self.assertTrue(any(t.get("id") == ticket_id for t in items))
        created = next((t for t in items if t.get("id") == ticket_id), None)
        self.assertIsNotNone(created)
        self.assertTrue(bool(created.get("ticket_number")))
        self.assertEqual(created.get("status"), "pending")
        self.assertIn("employee", created)
        self.assertEqual(created.get("employee", {}).get("id"), self.employee.id)

    def test_ticket_assignments_persist_on_current_project_plan(self):
        self.client.force_authenticate(user=self.admin)

        project = Project.objects.create(title="P", description="D", status="planned")
        plan = CurrentProjectPlan.objects.create(project=project, project_name="P")

        ticket = EmployeeTicket.objects.create(
            employee=self.employee,
            title="Investigate",
            description="",
            created_by=self.admin,
        )

        patch_payload = {
            "timeline": "t1",
            "ticket_assignments": [
                {
                    "ticket": ticket.id,
                    "employee": self.employee.id,
                    "assign_date": "2026-03-10",
                    "expire_date": "2026-03-20",
                }
            ],
        }

        res = self.client.patch(
            f"/api/private-projects/{project.id}/plan/",
            data=json.dumps(patch_payload),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 200)

        plan.refresh_from_db()
        self.assertEqual(plan.timeline, "t1")
        self.assertEqual(plan.ticket_assignments.count(), 1)
        ta = plan.ticket_assignments.first()
        self.assertEqual(ta.ticket_id, ticket.id)
        self.assertEqual(ta.employee_id, self.employee.id)

    def test_employee_can_post_and_fetch_ticket_comments(self):
        ticket = EmployeeTicket.objects.create(
            employee=self.employee,
            title="Comment me",
            description="",
            created_by=self.admin,
        )

        self.client.force_authenticate(user=self.emp_user)
        res = self.client.post(
            f"/api/employee-tickets/{ticket.id}/comments/",
            data={"text": "work update 1"},
            format="json",
        )
        self.assertEqual(res.status_code, 201)

        res2 = self.client.get(f"/api/employee-tickets/{ticket.id}/comments/")
        self.assertEqual(res2.status_code, 200)
        items = res2.json()
        self.assertTrue(any(c.get("text") == "work update 1" for c in items))

        res3 = self.client.get(f"/api/employee-ticket-comments/?ticket={ticket.id}")
        self.assertEqual(res3.status_code, 200)
        items3 = res3.json()
        self.assertTrue(any(c.get("text") == "work update 1" for c in items3))

        res4 = self.client.patch(
            f"/api/employee-tickets/{ticket.id}/",
            data={"employee_comment": "work update 2"},
            format="json",
        )
        self.assertEqual(res4.status_code, 200)
        res5 = self.client.get(f"/api/employee-tickets/{ticket.id}/comments/")
        self.assertEqual(res5.status_code, 200)
        items5 = res5.json()
        self.assertTrue(any(c.get("text") == "work update 2" for c in items5))

        res6 = self.client.patch(
            f"/api/employee-tickets/{ticket.id}/",
            data={"commenttext": "work update 3"},
            format="json",
        )
        self.assertEqual(res6.status_code, 200)

        res7 = self.client.patch(
            f"/api/employee-tickets/{ticket.id}/",
            data={"status": "in_progress"},
            format="json",
        )
        self.assertEqual(res7.status_code, 200)
        self.assertEqual(res7.json().get("status"), "in_progress")

    def test_admin_can_assign_and_unassign_via_patch(self):
        other_user = User.objects.create_user(
            username="emp2_ticket",
            email="emp2_ticket@example.com",
            phoneno="9000000005",
            password="pass1234",
        )
        other_employee = EmployeeProfile.objects.create(
            user=other_user,
            employee_id="DI30002",
            phone="9000000005",
            designation="Dev",
            status="active",
        )

        ticket = EmployeeTicket.objects.create(
            employee=self.employee,
            title="Assign me",
            description="",
            created_by=self.admin,
        )

        self.client.force_authenticate(user=self.admin)
        res = self.client.patch(
            f"/api/employee-tickets/{ticket.id}/",
            data={"assigned_to": other_employee.id, "reason": "Initial assignment"},
            format="json",
        )
        self.assertEqual(res.status_code, 200)

        res2 = self.client.get(f"/api/employee-tickets/{ticket.id}/")
        self.assertEqual(res2.status_code, 200)
        body = res2.json()
        self.assertEqual(body.get("assigned_to", {}).get("id"), other_employee.id)
        self.assertTrue(bool(body.get("assigned_at")))
        self.assertTrue(len(body.get("assignment_history", [])) >= 1)

        res3 = self.client.patch(
            f"/api/employee-tickets/{ticket.id}/",
            data={"assigned_to": None, "reason": "Unassign"},
            format="json",
        )
        self.assertEqual(res3.status_code, 200)
        res4 = self.client.get(f"/api/employee-tickets/{ticket.id}/")
        self.assertEqual(res4.status_code, 200)
        self.assertIsNone(res4.json().get("assigned_to"))
