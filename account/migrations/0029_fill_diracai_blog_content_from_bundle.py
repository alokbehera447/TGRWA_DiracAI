from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0028_fill_diracai_blog_content_placeholders"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop, migrations.RunPython.noop),
    ]

