from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0027_sync_diracai_blog_content"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop, migrations.RunPython.noop),
    ]

