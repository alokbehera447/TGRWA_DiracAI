from django.test import TestCase
from rest_framework.test import APIClient

from account.models import Project


class PublicProjectsPayloadTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project = Project.objects.create(
            title="Public Proj",
            description="D",
            status="planned",
            category="mobile",
        )

    def test_projects_list_does_not_include_employee_team_members(self):
        res = self.client.get("/api/projects/")
        self.assertEqual(res.status_code, 200)
        items = res.json()
        self.assertTrue(any(p.get("id") == self.project.id for p in items))
        for p in items:
            self.assertNotIn("employee_team_members", p)
            self.assertNotIn("employee_team_members_data", p)

    def test_projects_detail_does_not_include_employee_team_members(self):
        res = self.client.get(f"/api/projects/{self.project.id}/")
        self.assertEqual(res.status_code, 200)
        payload = res.json()
        self.assertNotIn("employee_team_members", payload)
        self.assertNotIn("employee_team_members_data", payload)
