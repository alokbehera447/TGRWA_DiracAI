from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0029_fill_diracai_blog_content_from_bundle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="category",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="blog",
            name="author_name",
            field=models.CharField(blank=True, default="", max_length=120),
        ),
    ]
