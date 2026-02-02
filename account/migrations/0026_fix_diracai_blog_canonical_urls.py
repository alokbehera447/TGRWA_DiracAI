from django.db import migrations


DIRACAI_SLUGS = [
    "why-public-sector-units-should-leverage-data-analytics",
    "ai-based-student-assessment-helps-educational-institutions",
    "why-startup-should-work-on-building-mvp",
    "future-of-web-development-trends",
    "blockchain-technology-revolutionizing-digital-transactions",
    "digital-marketing-strategies-modern-businesses",
]


def fix_canonical_urls(apps, schema_editor):
    Blog = apps.get_model("account", "Blog")

    for slug in DIRACAI_SLUGS:
        expected = f"https://diracai.com/blogs/{slug}"
        old = f"https://diracai.com/blog/{slug}"

        (
            Blog.objects.filter(slug=slug)
            .filter(canonical_url__in=["", old])
            .update(canonical_url=expected)
        )


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0025_sync_diracai_blog_posts"),
    ]

    operations = [
        migrations.RunPython(fix_canonical_urls, migrations.RunPython.noop),
    ]

