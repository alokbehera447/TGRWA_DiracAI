from django.db import migrations


def seed_blogs(apps, schema_editor):
    Blog = apps.get_model("account", "Blog")
    seed = [
        {
            "slug": "why-public-sector-units-should-leverage-data-analytics",
            "title": "Why Public Sector Units Should Leverage Data Analytics",
            "excerpt": "Public Sector Units can improve planning, efficiency, transparency, and citizen outcomes by leveraging data analytics across operations.",
            "content": "Public Sector Units can improve planning, efficiency, transparency, and citizen outcomes by leveraging data analytics across operations.",
            "category": "Analytics",
            "tags": ["data-analytics", "public-sector"],
            "status": "published",
            "canonical_url": "",
            "meta_title": "Why Public Sector Units Should Leverage Data Analytics",
            "meta_description": "Why Public Sector Units should leverage data analytics for better outcomes.",
        },
        {
            "slug": "rera-odisha-overview",
            "title": "Everything You Need To Know About RERA Odisha",
            "excerpt": "The emergence of the Real Estate Regulatory Authority brought a paradigm shift in the realty sector of Odisha. There were many conflicts between the buyers and sellers of real estate in the past.",
            "content": "The emergence of the Real Estate Regulatory Authority brought a paradigm shift in the realty sector of Odisha. There were many conflicts between the buyers and sellers of real estate in the past.",
            "category": "Real Estate",
            "tags": ["rera", "odisha", "regulation"],
            "status": "published",
            "canonical_url": "https://www.squareyards.com/blog/rera-odisha-rerat",
            "meta_title": "Everything You Need To Know About RERA Odisha",
            "meta_description": "Overview of the Real Estate Regulatory Authority in Odisha and its impact on the market.",
        },
        {
            "slug": "society-maintenance-charges",
            "title": "All You Need To Know About Society Maintenance Charges",
            "excerpt": "Once you are the rightful owner of a residence in a housing society, you are part of a larger community. Homeownership is a matter of pride and a lifelong commitment.",
            "content": "Once you are the rightful owner of a residence in a housing society, you are part of a larger community. Homeownership is a matter of pride and a lifelong commitment.",
            "category": "Housing",
            "tags": ["housing", "maintenance", "society"],
            "status": "published",
            "canonical_url": "https://mygate.com/blog/cooperative-housing-society/society-maintenance-charges/",
            "meta_title": "All You Need To Know About Society Maintenance Charges",
            "meta_description": "A quick guide to understanding housing society maintenance charges.",
        },
        {
            "slug": "apartment-pet-policies",
            "title": "Apartment Pet Policies: A Comprehensive Guide to Rules and Regulations",
            "excerpt": "When it comes to apartment hunting, pet owners face a unique set of challenges. Finding a place that accommodates furry family members can be a daunting task.",
            "content": "When it comes to apartment hunting, pet owners face a unique set of challenges. Finding a place that accommodates furry family members can be a daunting task.",
            "category": "Lifestyle",
            "tags": ["pets", "apartments", "rules"],
            "status": "published",
            "canonical_url": "https://adda.io/blog/2023/04/apartment-pet-policies/",
            "meta_title": "Apartment Pet Policies: A Comprehensive Guide to Rules and Regulations",
            "meta_description": "Rules and regulations for pet owners in apartment communities.",
        },
        {
            "slug": "housing-society-byelaws-member-rights",
            "title": "Housing Society Byelaws & Member Rights",
            "excerpt": "A housing society meeting may not appeal to you, especially if petty matters are discussed. It can be exhausting knowing your water pump will be fixed or when your sinking fund will be used.",
            "content": "A housing society meeting may not appeal to you, especially if petty matters are discussed. It can be exhausting knowing your water pump will be fixed or when your sinking fund will be used.",
            "category": "Housing",
            "tags": ["housing", "byelaws", "rights"],
            "status": "published",
            "canonical_url": "https://vakilsearch.com/blog/housing-society-byelaws-member-rights/",
            "meta_title": "Housing Society Byelaws & Member Rights",
            "meta_description": "Member rights and byelaws overview for housing societies.",
        },
    ]
    for item in seed:
        Blog.objects.get_or_create(
            slug=item["slug"],
            defaults={
                "title": item["title"],
                "excerpt": item["excerpt"],
                "content": item["content"],
                "category": item["category"],
                "tags": item["tags"],
                "status": item["status"],
                "canonical_url": item["canonical_url"],
                "meta_title": item["meta_title"],
                "meta_description": item["meta_description"],
            },
        )


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0023_alter_blog_author_avatar_url_and_more"),
    ]

    operations = [
        migrations.RunPython(seed_blogs, migrations.RunPython.noop),
    ]
