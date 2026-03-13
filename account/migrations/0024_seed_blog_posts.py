from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0023_alter_blog_author_avatar_url_and_more"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop, migrations.RunPython.noop),
    ]
