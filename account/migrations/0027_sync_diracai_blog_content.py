import datetime
import json
import re
import urllib.request

from django.db import migrations
from django.utils import timezone


def _parse_published_at(value: str):
    if not value:
        return None
    dt = datetime.datetime.strptime(value, "%b %d, %Y")
    tz = timezone.get_current_timezone()
    return timezone.make_aware(dt, tz)


def _fetch_text(url: str, headers: dict[str, str] | None = None, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "ignore")


def _extract_posts_chunk_url(rsc_text: str) -> str | None:
    m = re.search(r"static/chunks/645-[A-Za-z0-9]+\\.js", rsc_text)
    if not m:
        return None
    return "https://diracai.com/_next/" + m.group(0)


def _extract_js_array(js_text: str) -> str | None:
    ms = js_text.find("let i=")
    if ms == -1:
        return None
    start = js_text.find("[", ms)
    if start == -1:
        return None

    pos = start
    depth = 0
    in_str = None
    esc = False

    while pos < len(js_text):
        ch = js_text[pos]
        if in_str:
            if esc:
                esc = False
            elif ch == chr(92):
                esc = True
            elif ch == in_str:
                in_str = None
        else:
            if ch == chr(34) or ch == chr(39):
                in_str = ch
            elif ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0 and pos != start:
                    return js_text[start : pos + 1]
        pos += 1

    return None


def _parse_posts_from_bundle(js_text: str) -> list[dict] | None:
    arr = _extract_js_array(js_text)
    if not arr:
        return None

    json_text = re.sub(
        r"([\{,])\s*([A-Za-z_][A-Za-z0-9_]*)\s*:",
        lambda m: m.group(1) + chr(34) + m.group(2) + chr(34) + ":",
        arr,
    )
    return json.loads(json_text)


def sync_diracai_blog_content(apps, schema_editor):
    Blog = apps.get_model("account", "Blog")

    slugs = [
        "why-public-sector-units-should-leverage-data-analytics",
        "ai-based-student-assessment-helps-educational-institutions",
        "why-startup-should-work-on-building-mvp",
        "future-of-web-development-trends",
        "blockchain-technology-revolutionizing-digital-transactions",
        "digital-marketing-strategies-modern-businesses",
    ]

    try:
        probe_slug = slugs[0]
        tree = [
            "",
            {
                "children": [
                    "blog",
                    {
                        "children": [
                            ["slug", probe_slug, "d"],
                            {"children": ["__PAGE__", {}, None, None]},
                        ]
                    },
                    None,
                    None,
                ]
            },
            None,
            None,
            True,
        ]
        rsc = _fetch_text(
            f"https://diracai.com/blog/{probe_slug}?_rsc=1",
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "*/*",
                "RSC": "1",
                "Next-Url": f"/blog/{probe_slug}",
                "Next-Router-State-Tree": json.dumps(tree, separators=(",", ":")),
            },
            timeout=30,
        )
        bundle_url = _extract_posts_chunk_url(rsc)
        if not bundle_url:
            return
        bundle_js = _fetch_text(bundle_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
        posts = _parse_posts_from_bundle(bundle_js)
        if not posts:
            return
    except Exception:
        return

    posts_by_slug = {p.get("slug"): p for p in posts if isinstance(p, dict) and p.get("slug")}

    for slug in slugs:
        p = posts_by_slug.get(slug)
        if not p:
            continue

        image_url = (p.get("image") or "").strip()
        if image_url.startswith("/"):
            image_url = "https://diracai.com" + image_url

        author = p.get("author") if isinstance(p.get("author"), dict) else {}
        author_avatar_url = (author.get("avatar") or "").strip()
        if author_avatar_url.startswith("/"):
            author_avatar_url = "https://diracai.com" + author_avatar_url

        canonical = f"https://diracai.com/blogs/{slug}"
        published_at = _parse_published_at((p.get("date") or "").strip())

        defaults = {
            "title": (p.get("title") or "").strip(),
            "excerpt": (p.get("excerpt") or "").strip(),
            "content": (p.get("content") or "").strip(),
            "category": (p.get("category") or "General").strip(),
            "tags": p.get("tags") if isinstance(p.get("tags"), list) else [],
            "status": "published",
            "banner_image_url": image_url,
            "author_name": (author.get("name") or "DiracAI Team").strip(),
            "author_role": (author.get("role") or "").strip(),
            "author_avatar_url": author_avatar_url,
            "meta_title": (p.get("title") or "").strip(),
            "meta_description": (p.get("excerpt") or "").strip(),
            "canonical_url": canonical,
            "allow_indexing": True,
            "featured": False,
            "published_at": published_at,
        }

        obj, created = Blog.objects.get_or_create(slug=slug, defaults=defaults)

        if created:
            continue

        created_at = getattr(obj, "created_at", None)
        updated_at = getattr(obj, "updated_at", None)
        is_unedited = bool(created_at and updated_at and created_at == updated_at)
        if not is_unedited:
            continue

        for field, value in defaults.items():
            setattr(obj, field, value)
        obj.save()


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0026_fix_diracai_blog_canonical_urls"),
    ]

    operations = [
        migrations.RunPython(sync_diracai_blog_content, migrations.RunPython.noop),
    ]

