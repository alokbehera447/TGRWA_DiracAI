from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0050_project_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentProjectPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('project_name', models.CharField(blank=True, max_length=255)),
                ('project_description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='current_project_plan', to='account.project')),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='CurrentProjectAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('work', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('assigned', 'Assigned'), ('in_progress', 'In Progress'), ('review', 'Review'), ('completed', 'Completed')], default='assigned', max_length=20)),
                ('admin_comment', models.TextField(blank=True)),
                ('employee_comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_project_assignments', to='account.employeeprofile')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='account.currentprojectplan')),
            ],
            options={
                'ordering': ['employee_id', '-updated_at'],
                'unique_together': {('plan', 'employee')},
            },
        ),
        migrations.CreateModel(
            name='CurrentProjectDailyUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_updates', to='account.currentprojectassignment')),
            ],
            options={
                'ordering': ['-date', '-created_at'],
            },
        ),
    ]

