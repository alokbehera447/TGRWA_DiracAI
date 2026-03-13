import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from account.models import Project
from account.employee_models import PrivateProjectPlan


User = get_user_model()


class PrivateProjectPayloadTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            username="admin_private_payload",
            email="admin_private_payload@example.com",
            phoneno="9000000031",
            password="pass1234",
        )
        self.admin.is_staff = True
        self.admin.save()

        self.project = Project.objects.create(title="Proj PP", description="D", status="planned")

    def test_private_projects_post_ignores_unknown_keys(self):
        self.client.force_authenticate(user=self.admin)
        payload = {
            "status": "ongoing",  # unknown for plan model
            "ticket_assignments": [],  # unknown for plan serializer
            "assignments": [],  # handled separately
            "employees": [],  # handled separately
            "project_name": "My Plan",
            "project_description": "Desc",
            "timeline": "t",
        }

        res = self.client.post(
            "/api/private-projects/",
            data=json.dumps(payload),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 201)
        self.assertTrue(PrivateProjectPlan.objects.filter(project__title="My Plan").exists())
