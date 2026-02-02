import datetime

from django.db import migrations
from django.utils import timezone


def _parse_published_at(value: str):
    if not value:
        return None
    dt = datetime.datetime.strptime(value, "%b %d, %Y")
    tz = timezone.get_current_timezone()
    return timezone.make_aware(dt, tz)


def sync_diracai_blogs(apps, schema_editor):
    Blog = apps.get_model("account", "Blog")

    seed = [
        {
            "slug": "why-public-sector-units-should-leverage-data-analytics",
            "title": "Why Public Sector Units should leverage Data Analytics into their Organizations?",
            "excerpt": "Leveraging data analytics in public sector units can offer numerous benefits and contribute to more effective and efficient governance...",
            "category": "Data Analytics",
            "tags": ["data analytics", "public sector"],
            "banner_image_url": "https://diracai.com/placeholder.svg?height=600&width=800&query=data analytics dashboard with charts and government building",
            "author_name": "Dr. Amir Patel",
            "author_role": "Data Science Director",
            "published_at": "Dec 15, 2024",
        },
        {
            "slug": "ai-based-student-assessment-helps-educational-institutions",
            "title": "How AI-based Student Assessment Helps Educational Institutions",
            "excerpt": "Artificial Intelligence (AI) is helping student assessment for several reasons, providing benefits to both educators and students...",
            "category": "AI & Education",
            "tags": ["ai", "education", "assessment"],
            "banner_image_url": "https://diracai.com/placeholder.svg?height=600&width=800&query=ai educational assessment with students and teacher using tablets",
            "author_name": "DiracAI Team",
            "author_role": "",
            "published_at": "Dec 10, 2024",
        },
        {
            "slug": "why-startup-should-work-on-building-mvp",
            "title": "10 Must Reasons Why a Startup Should Work on Building a MVP",
            "excerpt": "Building a Minimum Viable Product (MVP) is a common and strategic approach for startups. Here are ten reasons why startups should consider developing an MVP...",
            "category": "Startup",
            "tags": ["startup", "mvp"],
            "banner_image_url": "https://diracai.com/placeholder.svg?height=600&width=800&query=startup team working on minimum viable product on whiteboard",
            "author_name": "DiracAI Team",
            "author_role": "",
            "published_at": "Dec 5, 2024",
        },
        {
            "slug": "future-of-web-development-trends",
            "title": "The Future of Web Development: Trends to Watch in 2024",
            "excerpt": "Explore the latest trends in web development that are shaping the future of digital experiences and user interactions...",
            "category": "Web Development",
            "tags": ["web development", "trends"],
            "banner_image_url": "https://diracai.com/placeholder.svg?height=600&width=800&query=futuristic web development with holographic interface",
            "author_name": "DiracAI Team",
            "author_role": "",
            "published_at": "Nov 28, 2024",
        },
        {
            "slug": "blockchain-technology-revolutionizing-digital-transactions",
            "title": "Blockchain Technology: Revolutionizing Digital Transactions",
            "excerpt": "Understanding how blockchain technology is transforming the way we handle digital transactions and data security...",
            "category": "Blockchain",
            "tags": ["blockchain", "transactions", "security"],
            "banner_image_url": "https://diracai.com/placeholder.svg?height=600&width=800&query=blockchain technology visualization with connected blocks",
            "author_name": "DiracAI Team",
            "author_role": "",
            "published_at": "Nov 20, 2024",
        },
        {
            "slug": "digital-marketing-strategies-modern-businesses",
            "title": "Digital Marketing Strategies for Modern Businesses",
            "excerpt": "Discover effective digital marketing strategies that can help your business reach new heights in the digital landscape...",
            "category": "Digital Marketing",
            "tags": ["digital marketing", "strategy"],
            "banner_image_url": "https://diracai.com/placeholder.svg?height=600&width=800&query=digital marketing strategy meeting with analytics dashboard",
            "author_name": "DiracAI Team",
            "author_role": "",
            "published_at": "Nov 15, 2024",
        },
    ]

    for item in seed:
        canonical = f"https://diracai.com/blogs/{item['slug']}"
        published_at = _parse_published_at(item.get("published_at", ""))
        defaults = {
            "title": item["title"],
            "excerpt": item["excerpt"],
            "content": item["excerpt"],
            "category": item["category"],
            "tags": item["tags"],
            "status": "published",
            "banner_image_url": item.get("banner_image_url", "") or "",
            "author_name": item.get("author_name", "") or "DiracAI Team",
            "author_role": item.get("author_role", "") or "",
            "meta_title": item["title"],
            "meta_description": item["excerpt"],
            "canonical_url": canonical,
            "allow_indexing": True,
            "featured": False,
            "published_at": published_at,
        }

        obj, created = Blog.objects.get_or_create(
            slug=item["slug"],
            defaults=defaults,
        )

        if created:
            continue

        is_unedited = getattr(obj, "created_at", None) and getattr(obj, "updated_at", None) and obj.created_at == obj.updated_at
        if not is_unedited:
            continue

        for field, value in defaults.items():
            setattr(obj, field, value)
        obj.save()


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0024_seed_blog_posts"),
    ]

    operations = [
        migrations.RunPython(sync_diracai_blogs, migrations.RunPython.noop),
    ]
