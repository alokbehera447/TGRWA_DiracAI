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


def _discover_bundle_url(slug: str) -> str | None:
    try:
        tree = [
            "",
            {
                "children": [
                    "blog",
                    {
                        "children": [
                            ["slug", slug, "d"],
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
            f"https://diracai.com/blog/{slug}?_rsc=1",
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "*/*",
                "RSC": "1",
                "Next-Url": f"/blog/{slug}",
                "Next-Router-State-Tree": json.dumps(tree, separators=(",", ":")),
            },
            timeout=30,
        )
        m = re.search(r"static/chunks/645-[A-Za-z0-9]+\\.js", rsc)
        if m:
            return "https://diracai.com/_next/" + m.group(0)
    except Exception:
        pass

    return "https://diracai.com/_next/static/chunks/645-f08fd3c33be8588d.js"


def fill_diracai_blog_content_from_bundle(apps, schema_editor):
    Blog = apps.get_model("account", "Blog")

    slugs = [
        "why-public-sector-units-should-leverage-data-analytics",
        "ai-based-student-assessment-helps-educational-institutions",
        "why-startup-should-work-on-building-mvp",
        "future-of-web-development-trends",
        "blockchain-technology-revolutionizing-digital-transactions",
        "digital-marketing-strategies-modern-businesses",
    ]

    bundle_url = _discover_bundle_url(slugs[0])
    if not bundle_url:
        return

    try:
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

        remote_title = (p.get("title") or "").strip()
        remote_excerpt = (p.get("excerpt") or "").strip()
        remote_content = (p.get("content") or "").strip()
        remote_category = (p.get("category") or "General").strip()
        remote_tags = p.get("tags") if isinstance(p.get("tags"), list) else []
        remote_date = (p.get("date") or "").strip()
        published_at = _parse_published_at(remote_date)

        remote_image_url = (p.get("image") or "").strip()
        if remote_image_url.startswith("/"):
            remote_image_url = "https://diracai.com" + remote_image_url

        author = p.get("author") if isinstance(p.get("author"), dict) else {}
        remote_author_name = (author.get("name") or "DiracAI Team").strip()
        remote_author_role = (author.get("role") or "").strip()
        remote_author_avatar_url = (author.get("avatar") or "").strip()
        if remote_author_avatar_url.startswith("/"):
            remote_author_avatar_url = "https://diracai.com" + remote_author_avatar_url

        canonical = f"https://diracai.com/blogs/{slug}"

        try:
            obj = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            obj = Blog(slug=slug)

        updates: dict[str, object] = {}

        if not getattr(obj, "title", "") and remote_title:
            updates["title"] = remote_title
        if not getattr(obj, "excerpt", "") and remote_excerpt:
            updates["excerpt"] = remote_excerpt

        current_content = (getattr(obj, "content", "") or "").strip()
        current_excerpt = (getattr(obj, "excerpt", "") or "").strip()
        content_is_placeholder = (not current_content) or (current_content == current_excerpt) or (len(current_content) < 300)
        if content_is_placeholder and remote_content:
            updates["content"] = remote_content

        if (getattr(obj, "category", "") or "").strip() in ["", "General"] and remote_category:
            updates["category"] = remote_category
        if not getattr(obj, "tags", None) and remote_tags:
            updates["tags"] = remote_tags

        if not getattr(obj, "banner_image_url", "") and remote_image_url:
            updates["banner_image_url"] = remote_image_url
        if (getattr(obj, "author_name", "") or "").strip() in ["", "DiracAI Team"] and remote_author_name:
            updates["author_name"] = remote_author_name
        if not getattr(obj, "author_role", "") and remote_author_role:
            updates["author_role"] = remote_author_role
        if not getattr(obj, "author_avatar_url", "") and remote_author_avatar_url:
            updates["author_avatar_url"] = remote_author_avatar_url

        if not getattr(obj, "meta_title", "") and remote_title:
            updates["meta_title"] = remote_title
        if not getattr(obj, "meta_description", "") and remote_excerpt:
            updates["meta_description"] = remote_excerpt
        if getattr(obj, "canonical_url", "") in ["", f"https://diracai.com/blog/{slug}"]:
            updates["canonical_url"] = canonical

        if not getattr(obj, "published_at", None) and published_at:
            updates["published_at"] = published_at

        if getattr(obj, "status", "") != "published":
            updates["status"] = "published"

        if not updates:
            continue

        for field, value in updates.items():
            setattr(obj, field, value)
        obj.save()


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0028_fill_diracai_blog_content_placeholders"),
    ]

    operations = [
        migrations.RunPython(fill_diracai_blog_content_from_bundle, migrations.RunPython.noop),
    ]

