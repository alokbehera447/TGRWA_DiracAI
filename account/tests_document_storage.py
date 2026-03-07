import os
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TransactionTestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

from account.employee_models import EmployeeDocument, EmployeeProfile


User = get_user_model()


class EmployeeDocumentStorageTests(TransactionTestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.raise_request_exception = False

        self.admin = User.objects.create_user(
            username="admin_doc_tester",
            email="admin-doc@test.com",
            phoneno="9000000001",
            password="pass123",
        )
        self.admin.is_staff = True
        self.admin.save()

        self.employee_user = User.objects.create_user(
            username="employee_doc_tester",
            email="employee-doc@test.com",
            phoneno="9000000002",
            password="pass123",
        )
        self.employee = EmployeeProfile.objects.create(
            user=self.employee_user,
            employee_id="DI90001",
            phone="+919000000002",
            designation="QA",
            status="active",
        )

    def _upload_document(self, filename, content, content_type, method="post", extra_fields=None):
        self.client.force_authenticate(user=self.admin)
        payload = {
            "document_file": SimpleUploadedFile(filename, content, content_type=content_type),
            "document_title": f"title-{filename}",
            "document_type": "test",
        }
        if extra_fields:
            payload.update(extra_fields)
        if method.lower() == "patch":
            response = self.client.patch(f"/api/employees/{self.employee.id}/", data=payload, format="multipart")
        else:
            response = self.client.post(f"/api/employees/{self.employee.id}/", data=payload, format="multipart")
        return response

    def _assert_success_response(self, response):
        self.assertEqual(response.status_code, 200)
        data = response.json()
        if isinstance(data, dict) and data.get("success") is False:
            self.fail(f"Expected success upload response, got wrapped error: {data}")

    @override_settings(DEBUG=True)
    def test_upload_pdf_success_and_content_integrity(self):
        original = b"%PDF-1.4\nfake-pdf-body\n"
        response = self._upload_document("sample.pdf", original, "application/pdf")
        self._assert_success_response(response)

        doc = EmployeeDocument.objects.latest("id")
        self.assertTrue(doc.file.name.endswith(".pdf"))
        with doc.file.open("rb") as fh:
            self.assertEqual(fh.read(), original)

    @override_settings(DEBUG=False)
    def test_upload_docx_success_and_content_integrity_in_production_mode(self):
        original = b"PK\x03\x04fake-docx-body"
        response = self._upload_document(
            "sample.docx",
            original,
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
        self._assert_success_response(response)

        doc = EmployeeDocument.objects.latest("id")
        self.assertTrue(doc.file.name.endswith(".docx"))
        with doc.file.open("rb") as fh:
            self.assertEqual(fh.read(), original)

    @override_settings(DEBUG=True)
    def test_retrieval_confirms_documents_exist_and_metadata_present(self):
        original = b"hello world"
        self._upload_document("meta.pdf", original, "application/pdf")
        response = self.client.get(f"/api/employees/{self.employee.id}/")
        self.assertEqual(response.status_code, 200)

        payload = response.json()
        docs = payload.get("documents", [])
        self.assertGreaterEqual(len(docs), 1)
        latest = docs[0]
        self.assertIn("uploaded_at", latest)
        self.assertIn("updated_at", latest)
        self.assertIn("document_url", latest)
        self.assertIn("title", latest)
        self.assertNotEqual(latest.get("document_url"), "")
        self.assertNotIn("file_url", latest)
        self.assertIn(f"/api/employees/{self.employee.id}/documents/", latest.get("document_url", ""))

    @override_settings(DEBUG=True)
    def test_empty_document_upload(self):
        response = self._upload_document("empty.pdf", b"", "application/pdf")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload.get("success"), False)
        self.assertEqual(int(payload.get("original_status", 0)), 400)
        error = payload.get("error", {})
        self.assertIn("file", error)

    @override_settings(DEBUG=True)
    def test_large_document_upload(self):
        large_bytes = os.urandom(5 * 1024 * 1024)
        response = self._upload_document("large.bin", large_bytes, "application/octet-stream")
        self._assert_success_response(response)
        doc = EmployeeDocument.objects.latest("id")
        with doc.file.open("rb") as fh:
            self.assertEqual(fh.read(), large_bytes)

    @override_settings(DEBUG=True)
    def test_special_characters_filename_upload(self):
        data = b"special-name-body"
        response = self._upload_document("r\xc3\xa9sum\xc3\xa9 @2026 #final (v1).docx", data, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        self._assert_success_response(response)
        doc = EmployeeDocument.objects.latest("id")
        self.assertIn("employee-documents/", doc.file.name)
        with doc.file.open("rb") as fh:
            self.assertEqual(fh.read(), data)

    @override_settings(DEBUG=True)
    def test_storage_unavailable_returns_failure_and_no_document_created(self):
        before = EmployeeDocument.objects.count()
        with patch("django.core.files.storage.FileSystemStorage._save", side_effect=OSError("Storage unavailable")):
            response = self._upload_document("fail.pdf", b"x", "application/pdf")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload.get("success"), False)
        self.assertGreaterEqual(int(payload.get("original_status", 500)), 500)
        self.assertEqual(EmployeeDocument.objects.count(), before)

    @override_settings(DEBUG=False)
    def test_quota_exceeded_error_in_production_mode(self):
        before = EmployeeDocument.objects.count()
        with patch("django.core.files.storage.FileSystemStorage._save", side_effect=OSError("No space left on device")):
            response = self._upload_document("quota.pdf", b"x", "application/pdf")
        self.assertGreaterEqual(response.status_code, 500)
        self.assertEqual(EmployeeDocument.objects.count(), before)

    @override_settings(DEBUG=True)
    def test_metadata_author_and_version_observation(self):
        self._upload_document("version-check.pdf", b"v1", "application/pdf")
        response = self.client.get(f"/api/employees/{self.employee.id}/")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        docs = payload.get("documents", [])
        self.assertGreaterEqual(len(docs), 1)
        latest = docs[0]
        self.assertIn("uploaded_at", latest)
        self.assertIn("updated_at", latest)
        self.assertNotIn("version", latest)
        self.assertIn("id", latest)
