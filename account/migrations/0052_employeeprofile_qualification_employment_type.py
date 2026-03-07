from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0051_current_project_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract'), ('intern', 'Intern'), ('consultant', 'Consultant')], max_length=30),
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='qualification',
            field=models.TextField(blank=True),
        ),
    ]

