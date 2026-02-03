import json

from django.test import TestCase
from django.utils import timezone

from account.models import Blog, BlogCategory, BlogComment


class PublicBlogAPITests(TestCase):
    def test_no_seeded_blogs(self):
        self.assertEqual(Blog.objects.count(), 0)

    def test_list_empty_returns_200_and_empty(self):
        res = self.client.get("/api/blogs/")
        self.assertEqual(res.status_code, 200)
        payload = res.json()
        items = payload.get("results", []) if isinstance(payload, dict) else payload
        self.assertEqual(items, [])

    def test_defaults_are_empty_strings(self):
        blog = Blog.objects.create(title="T", content="C", status="draft")
        self.assertEqual(blog.category, "")
        self.assertEqual(blog.author_name, "")

    def test_published_sets_published_at(self):
        blog = Blog.objects.create(title="Published", content="Hello world", status="published")
        self.assertIsNotNone(blog.published_at)

    def test_list_returns_only_published(self):
        draft = Blog.objects.create(title="Draft", content="X", status="draft")
        published = Blog.objects.create(
            title="Published",
            content="Hello world",
            status="published",
            published_at=timezone.now(),
        )

        res = self.client.get("/api/blogs/")
        self.assertEqual(res.status_code, 200)

        payload = res.json()
        items = payload.get("results", []) if isinstance(payload, dict) else payload
        slugs = {item.get("slug") for item in items}

        self.assertIn(published.slug, slugs)
        self.assertNotIn(draft.slug, slugs)

    def test_list_item_shape(self):
        published = Blog.objects.create(title="Published", content="Hello world", status="published")
        res = self.client.get("/api/blogs/")
        self.assertEqual(res.status_code, 200)

        payload = res.json()
        items = payload.get("results", []) if isinstance(payload, dict) else payload
        self.assertEqual(len(items), 1)
        item = items[0]

        for key in ["id", "slug", "title", "excerpt", "content", "category", "tags", "image", "author", "date", "readingTime"]:
            self.assertIn(key, item)
        self.assertEqual(item["slug"], published.slug)
        self.assertIsInstance(item["tags"], list)
        self.assertIsInstance(item["author"], dict)
        self.assertIn("name", item["author"])
        self.assertIn("role", item["author"])
        self.assertIn("avatar", item["author"])
        self.assertTrue(isinstance(item["readingTime"], int))

    def test_detail_returns_published_and_404_for_draft(self):
        draft = Blog.objects.create(title="Draft", content="X", status="draft")
        published = Blog.objects.create(
            title="Published",
            content="Hello world",
            status="published",
            published_at=timezone.now(),
        )

        res_ok = self.client.get(f"/api/blogs/{published.slug}/")
        self.assertEqual(res_ok.status_code, 200)
        self.assertEqual(res_ok.json().get("slug"), published.slug)

        res_missing = self.client.get(f"/api/blogs/{draft.slug}/")
        self.assertEqual(res_missing.status_code, 404)

    def test_detail_invalid_slug_returns_404(self):
        res = self.client.get("/api/blogs/does-not-exist/")
        self.assertEqual(res.status_code, 404)


class BlogCategoryAndCommentAPITests(TestCase):
    def test_category_list_returns_200(self):
        BlogCategory.objects.create(name="General")
        res = self.client.get("/api/blog-categories/")
        self.assertEqual(res.status_code, 200)
        payload = res.json()
        items = payload.get("results", []) if isinstance(payload, dict) else payload
        self.assertEqual(len(items), 1)
        item = items[0]
        self.assertIn("id", item)
        self.assertIn("name", item)
        self.assertIn("slug", item)
        self.assertEqual(item["name"], "General")

    def test_comments_list_returns_only_approved_for_published_blog(self):
        blog = Blog.objects.create(title="Published", content="Hello world", status="published")
        BlogComment.objects.create(blog=blog, name="A", email="a@example.com", content="Ok", status="approved")
        BlogComment.objects.create(blog=blog, name="B", email="b@example.com", content="No", status="pending")

        res = self.client.get(f"/api/blogs/{blog.slug}/comments/")
        self.assertEqual(res.status_code, 200)
        payload = res.json()
        items = payload.get("results", []) if isinstance(payload, dict) else payload
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["name"], "A")

    def test_comments_list_returns_404_for_draft_blog(self):
        blog = Blog.objects.create(title="Draft", content="X", status="draft")
        res = self.client.get(f"/api/blogs/{blog.slug}/comments/")
        self.assertEqual(res.status_code, 404)

    def test_comment_post_creates_pending_comment_and_strips_html(self):
        blog = Blog.objects.create(title="Published", content="Hello world", status="published")

        res = self.client.post(
            f"/api/blogs/{blog.slug}/comments/",
            data=json.dumps({"name": "Anon", "email": "anon@example.com", "content": "<b>Hello</b>"}),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 201)
        self.assertEqual(BlogComment.objects.filter(blog=blog).count(), 1)
        comment = BlogComment.objects.get(blog=blog)
        self.assertEqual(comment.status, "pending")
        self.assertEqual(comment.content, "Hello")
