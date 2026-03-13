from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0053_currentprojectplan_timeline"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeTicket",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("status", models.CharField(choices=[("open", "Open"), ("in_progress", "In Progress"), ("resolved", "Resolved"), ("closed", "Closed")], default="open", max_length=20)),
                ("priority", models.CharField(choices=[("low", "Low"), ("medium", "Medium"), ("high", "High"), ("urgent", "Urgent")], default="medium", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="created_employee_tickets", to="account.account")),
                ("employee", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="tickets", to="account.employeeprofile")),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="CurrentProjectTicketAssignment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("assign_date", models.DateField(blank=True, null=True)),
                ("expire_date", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("employee", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="current_project_ticket_assignments", to="account.employeeprofile")),
                ("plan", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="ticket_assignments", to="account.currentprojectplan")),
                ("ticket", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="plan_assignments", to="account.employeeticket")),
            ],
            options={
                "ordering": ["-updated_at"],
                "unique_together": {("plan", "employee", "ticket")},
            },
        ),
    ]
