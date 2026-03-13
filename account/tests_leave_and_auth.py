from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from account.employee_models import EmployeeProfile, LeaveRequest


User = get_user_model()


class LeaveBalanceAndLogoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="emp_leave",
            email="emp_leave@example.com",
            phoneno="9000000021",
            password="pass1234",
        )
        self.employee = EmployeeProfile.objects.create(
            user=self.user,
            employee_id="DI50001",
            phone="9000000021",
            designation="Developer",
            status="active",
        )

    def test_leave_balance_is_monthly_and_resets_to_24_total(self):
        today = date.today()
        current_month_start = today.replace(day=1)
        next_month_start = date(today.year + 1, 1, 1) if today.month == 12 else date(today.year, today.month + 1, 1)

        LeaveRequest.objects.create(
            employee=self.employee,
            start_date=current_month_start,
            end_date=current_month_start + timedelta(days=2),
            status="approved",
        )
        LeaveRequest.objects.create(
            employee=self.employee,
            start_date=current_month_start - timedelta(days=2),
            end_date=current_month_start + timedelta(days=1),
            status="approved",
        )
        LeaveRequest.objects.create(
            employee=self.employee,
            start_date=next_month_start,
            end_date=next_month_start + timedelta(days=1),
            status="approved",
        )

        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/leave-balance/")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["total"], 24)
        self.assertEqual(payload["used"], 5)
        self.assertEqual(payload["remaining"], 19)
        self.assertEqual(payload["month"], today.month)

    def test_api_logout_clears_auth_cookies(self):
        self.client.cookies["access_token"] = "access-value"
        self.client.cookies["refresh_token"] = "refresh-value"

        response = self.client.post("/api/logout/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.cookies)
        self.assertIn("refresh_token", response.cookies)
        self.assertEqual(response.cookies["access_token"].value, "")
        self.assertEqual(response.cookies["refresh_token"].value, "")
