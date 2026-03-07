from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0058_currentprojectassignment_designation"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employeeprofile",
            old_name="current_project",
            new_name="private_project",
        ),
        migrations.CreateModel(
            name="PrivateProjectPlan",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("timeline", models.CharField(blank=True, max_length=255)),
                ("project_name", models.CharField(blank=True, max_length=255)),
                ("project_description", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "project",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="private_project_plan",
                        to="account.project",
                    ),
                ),
            ],
            options={
                "ordering": ["-updated_at"],
            },
        ),
        migrations.CreateModel(
            name="PrivateProjectAssignment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("designation", models.CharField(blank=True, default="", max_length=120)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("work", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("assigned", "Assigned"),
                            ("in_progress", "In Progress"),
                            ("review", "Review"),
                            ("completed", "Completed"),
                        ],
                        default="assigned",
                        max_length=20,
                    ),
                ),
                ("admin_comment", models.TextField(blank=True)),
                ("employee_comment", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="private_project_assignments",
                        to="account.employeeprofile",
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignments",
                        to="account.privateprojectplan",
                    ),
                ),
            ],
            options={
                "ordering": ["employee_id", "-updated_at"],
                "unique_together": {("plan", "employee")},
            },
        ),
        migrations.CreateModel(
            name="PrivateProjectDailyUpdate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField()),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "assignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="daily_updates",
                        to="account.privateprojectassignment",
                    ),
                ),
            ],
            options={
                "ordering": ["-date", "-created_at"],
            },
        ),
        migrations.CreateModel(
            name="PrivateProjectTicketAssignment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("assign_date", models.DateField(blank=True, null=True)),
                ("expire_date", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="private_project_ticket_assignments",
                        to="account.employeeprofile",
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ticket_assignments",
                        to="account.privateprojectplan",
                    ),
                ),
                (
                    "ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="private_plan_assignments",
                        to="account.employeeticket",
                    ),
                ),
            ],
            options={
                "ordering": ["-updated_at"],
                "unique_together": {("plan", "employee", "ticket")},
            },
        ),
    ]

