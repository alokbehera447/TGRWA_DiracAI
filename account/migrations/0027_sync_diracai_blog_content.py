from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0026_fix_diracai_blog_canonical_urls"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop, migrations.RunPython.noop),
    ]

