from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0052_employeeprofile_qualification_employment_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="currentprojectplan",
            name="timeline",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

