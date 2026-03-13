from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Optional

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.test import Client
from rest_framework_simplejwt.tokens import RefreshToken

from account.employee_models import EmployeeProfile


User = get_user_model()


@dataclass(frozen=True)
class ProbeResult:
    path: str
    method: str
    mode: str
    status_code: int
    original_status: Optional[int]
    detail: str


def _admin_token() -> Optional[str]:
    admin = User.objects.filter(is_staff=True).first() or User.objects.filter(is_superuser=True).first()
    if not admin:
        return None
    return str(RefreshToken.for_user(admin).access_token)


def _employee_token() -> Optional[str]:
    emp = EmployeeProfile.objects.select_related("user").first()
    if not emp:
        return None
    return str(RefreshToken.for_user(emp.user).access_token)


def _extract_detail(resp) -> tuple[Optional[int], str]:
    try:
        payload = json.loads(resp.content.decode("utf-8"))
    except Exception:
        return None, ""
    if isinstance(payload, dict) and "original_status" in payload:
        orig = payload.get("original_status")
        err = payload.get("error")
        if isinstance(err, dict) and "detail" in err:
            return int(orig) if isinstance(orig, int) else None, str(err.get("detail") or "")
        return int(orig) if isinstance(orig, int) else None, json.dumps(err)[:240]
    if isinstance(payload, dict) and "detail" in payload:
        return None, str(payload.get("detail") or "")
    return None, ""


def _probe(client: Client, path: str, method: str, mode: str, token: Optional[str]) -> ProbeResult:
    extra: dict[str, Any] = {"HTTP_HOST": "127.0.0.1"}
    if token:
        extra["HTTP_AUTHORIZATION"] = "JWT " + token

    if method == "OPTIONS":
        resp = client.options(
            path,
            HTTP_ORIGIN="http://localhost:3000",
            HTTP_ACCESS_CONTROL_REQUEST_METHOD="GET",
            HTTP_ACCESS_CONTROL_REQUEST_HEADERS="authorization,content-type",
            **extra,
        )
    elif method == "GET":
        resp = client.get(path, **extra)
    elif method == "POST":
        resp = client.post(path, data=json.dumps({}), content_type="application/json", **extra)
    elif method == "PATCH":
        resp = client.patch(path, data=json.dumps({}), content_type="application/json", **extra)
    elif method == "DELETE":
        resp = client.delete(path, **extra)
    else:
        raise ValueError(method)

    orig, detail = _extract_detail(resp)
    return ProbeResult(
        path=path,
        method=method,
        mode=mode,
        status_code=int(resp.status_code),
        original_status=orig,
        detail=detail,
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = Client()
        try:
            client.raise_request_exception = False
        except Exception:
            pass

        admin_token = _admin_token()
        employee_token = _employee_token()

        endpoints = [
            "/api/employees/",
            "/api/employees/me/",
            "/api/employees/1/",
            "/api/employees/1/set-password/",
            "/api/employees/projects/",
            "/api/employees/projects/1/",
            "/api/employee-documents/",
            "/api/employee-documents/1/",
            "/api/leave-balance/",
            "/api/leave-requests/",
            "/api/leave-requests/1/",
            "/api/overtime-requests/",
            "/api/overtime-requests/1/",
            "/api/employee/login/request/",
            "/api/employee/otp/verify/",
            "/api/employee/otp/resend/",
        ]

        methods = ["OPTIONS", "GET"]
        results: list[ProbeResult] = []
        for path in endpoints:
            for method in methods:
                results.append(_probe(client, path, method, "anon", None))
                results.append(_probe(client, path, method, "admin", admin_token))
                results.append(_probe(client, path, method, "employee", employee_token))

        server_errors = [
            r
            for r in results
            if (r.original_status is not None and r.original_status >= 500) or (r.original_status is None and r.status_code >= 500)
        ]

        self.stdout.write(
            json.dumps(
                {
                    "summary": {
                        "endpoints": len(endpoints),
                        "probes": len(results),
                        "server_errors": len(server_errors),
                    },
                    "server_errors": [r.__dict__ for r in server_errors],
                },
                indent=2,
            )
        )
