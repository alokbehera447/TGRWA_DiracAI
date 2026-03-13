from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0024_seed_blog_posts"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop, migrations.RunPython.noop),
    ]
