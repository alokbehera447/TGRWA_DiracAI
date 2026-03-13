from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0057_projectmembership"),
    ]

    operations = [
        migrations.AddField(
            model_name="currentprojectassignment",
            name="designation",
            field=models.CharField(blank=True, default="", max_length=120),
        ),
    ]

