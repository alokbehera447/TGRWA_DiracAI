import json

from django.test import TestCase
from rest_framework.test import APIClient
from django.utils import timezone

from account.models import Blog, BlogCategory, BlogComment, Service, GisService
from django.utils.text import slugify


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


class ServiceAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.service1 = Service.objects.create(
            title="Alpha Service",
            description="first",
            status="active",
        )
        self.service2 = Service.objects.create(
            title="Beta Service",
            description="second",
            status="inactive",
        )

        from django.contrib.auth import get_user_model
        User = get_user_model()
        self.admin = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            phoneno="0000000000",
            password="pass",
        )
        self.admin.is_staff = True
        self.admin.save()

    def test_slug_auto_generation_and_id(self):
        self.assertEqual(self.service1.slug, slugify(self.service1.title))
        self.assertEqual(self.service1.id, self.service1.slug)

    def test_public_list_only_active(self):
        res = self.client.get("/api/services/")
        self.assertEqual(res.status_code, 200)
        payload = res.json()
        items = payload.get("results", []) if isinstance(payload, dict) else payload
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["slug"], self.service1.slug)

    def test_public_list_supports_status_and_exclude(self):
        res = self.client.get(f"/api/services/?status=inactive")
        self.assertEqual(res.status_code, 200)
        items = res.json()
        items = items.get("results", []) if isinstance(items, dict) else items
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["slug"], self.service2.slug)

        res2 = self.client.get(f"/api/services/?exclude={self.service1.id}")
        self.assertEqual(res2.status_code, 200)
        items2 = res2.json()
        items2 = items2.get("results", []) if isinstance(items2, dict) else items2
        self.assertEqual(len(items2), 0)

    def test_admin_list_returns_all(self):
        self.client.force_authenticate(user=self.admin)
        res = self.client.get("/api/services/")
        self.assertEqual(res.status_code, 200)
        payload = res.json()
        items = payload.get("results", []) if isinstance(payload, dict) else payload
        self.assertEqual(len(items), 2)

    def test_admin_crud_requires_auth(self):
        data = {"title": "New", "description": "x"}
        res = self.client.post("/api/services/", data)
        self.assertEqual(res.status_code, 403)

        self.client.force_authenticate(user=self.admin)
        res2 = self.client.post("/api/services/", data)
        self.assertIn(res2.status_code, (200, 201))


class GisServiceAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.service1 = GisService.objects.create(
            title="Alpha GIS Service",
            description="first",
            status="active",
        )
        self.service2 = GisService.objects.create(
            title="Beta GIS Service",
            description="second",
            status="inactive",
        )

        from django.contrib.auth import get_user_model
        User = get_user_model()
        self.admin = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            phoneno="0000000000",
            password="pass",
        )
        self.admin.is_staff = True
        self.admin.save()

    def test_slug_auto_generation_and_id(self):
        self.assertEqual(self.service1.slug, slugify(self.service1.title))
        self.assertEqual(self.service1.id, self.service1.slug)

    def test_public_list_only_active(self):
        res = self.client.get("/api/gis-services/")
        self.assertEqual(res.status_code, 200)
        payload = res.json()
        items = payload.get("results", []) if isinstance(payload, dict) else payload
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["slug"], self.service1.slug)

    def test_public_list_supports_status_and_exclude(self):
        res = self.client.get(f"/api/gis-services/?status=inactive")
        self.assertEqual(res.status_code, 200)
        items = res.json()
        items = items.get("results", []) if isinstance(items, dict) else items
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["slug"], self.service2.slug)

        res2 = self.client.get(f"/api/gis-services/?exclude={self.service1.id}")
        self.assertEqual(res2.status_code, 200)
        items2 = res2.json()
        items2 = items2.get("results", []) if isinstance(items2, dict) else items2
        self.assertEqual(len(items2), 0)

    def test_admin_list_returns_all(self):
        self.client.force_authenticate(user=self.admin)
        res = self.client.get("/api/gis-services/")
        self.assertEqual(res.status_code, 200)
        payload = res.json()
        items = payload.get("results", []) if isinstance(payload, dict) else payload
        self.assertEqual(len(items), 2)

    def test_slug_endpoint_public(self):
        res = self.client.get(f"/api/gis-services/by-slug/{self.service1.slug}/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get("slug"), self.service1.slug)

        res_inactive = self.client.get(f"/api/gis-services/by-slug/{self.service2.slug}/")
        self.assertEqual(res_inactive.status_code, 404)

    def test_slug_endpoint_not_found(self):
        res = self.client.get("/api/gis-services/by-slug/nonexistent/")
        self.assertEqual(res.status_code, 404)

    def test_admin_crud_requires_auth(self):
        data = {"title": "New", "description": "x"}
        res = self.client.post("/api/gis-services/", data)
        self.assertEqual(res.status_code, 403)

        self.client.force_authenticate(user=self.admin)
        res2 = self.client.post("/api/gis-services/", data)
        self.assertIn(res2.status_code, (200, 201))
