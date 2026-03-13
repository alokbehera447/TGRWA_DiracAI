from __future__ import annotations

import json
import io
from dataclasses import dataclass
from typing import Any, Optional

from contextlib import redirect_stderr, redirect_stdout
from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import get_resolver
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model

from account.employee_models import EmployeeProfile
from account.models import GalleryItem, GisService, Product, Project, Service


User = get_user_model()


@dataclass(frozen=True)
class ProbeResult:
    path: str
    method: str
    authed: bool
    status_code: int
    cors_allow_origin: Optional[str]
    detail: str


def _first_id(qs, default: int = 1) -> int:
    obj = qs.first()
    return int(getattr(obj, "id", default) or default)

def _first_pk(qs, default: str = "1") -> str:
    obj = qs.first()
    if not obj:
        return default
    pk = getattr(obj, "pk", None) or getattr(obj, "id", None)
    return str(pk) if pk is not None else default


def _example_path(raw: str) -> str:
    if "<int:pk>" in raw:
        if "/employees/" in raw:
            raw = raw.replace("<int:pk>", str(_first_id(EmployeeProfile.objects.all(), 1)))
        elif "/projects/" in raw:
            raw = raw.replace("<int:pk>", str(_first_id(Project.objects.all(), 1)))
        elif "/gallery/" in raw:
            raw = raw.replace("<int:pk>", str(_first_id(GalleryItem.objects.all(), 1)))
        elif "/products/" in raw:
            raw = raw.replace("<int:pk>", str(_first_id(Product.objects.all(), 1)))
        else:
            raw = raw.replace("<int:pk>", "1")
    if "<str:pk>" in raw:
        if "/services/" in raw:
            raw = raw.replace("<str:pk>", _first_pk(Service.objects.all(), "1"))
        elif "/gis-services/" in raw:
            raw = raw.replace("<str:pk>", _first_pk(GisService.objects.all(), "1"))
        else:
            raw = raw.replace("<str:pk>", "1")
    if "<slug:slug>" in raw:
        raw = raw.replace("<slug:slug>", "test")
    if "<slug:service_slug>" in raw:
        raw = raw.replace("<slug:service_slug>", "test")
    if "<slug:sub_slug>" in raw:
        raw = raw.replace("<slug:sub_slug>", "test")
    if "<int:num>" in raw:
        raw = raw.replace("<int:num>", "5")
    raw = raw.replace("<str:speakername>", "test")
    raw = raw.replace("<username>", "admin")
    return raw


def _iter_api_paths() -> list[str]:
    resolver = get_resolver()
    out: list[str] = []
    stack = list(resolver.url_patterns)
    while stack:
        p = stack.pop(0)
        if hasattr(p, "url_patterns"):
            stack.extend(list(p.url_patterns))
            continue
        route = getattr(getattr(p, "pattern", None), "_route", None)
        if not isinstance(route, str):
            continue
        if "api/" not in route and not route.startswith("api/"):
            continue
        if route.startswith("/"):
            route = route[1:]
        if not route.startswith("api/"):
            idx = route.find("api/")
            route = route[idx:]
        if not route.startswith("api/"):
            continue
        if not route.endswith("/"):
            route = route + "/"
        out.append("/" + route)
    out = sorted(set(out))
    return [_example_path(x) for x in out]


def _get_admin_token() -> Optional[str]:
    admin = User.objects.filter(is_staff=True).first() or User.objects.filter(is_superuser=True).first()
    if not admin:
        admin = User.objects.first()
    if not admin:
        return None
    return str(RefreshToken.for_user(admin).access_token)


def _probe(client: Client, path: str, method: str, authed: bool, token: Optional[str]) -> ProbeResult:
    extra: dict[str, Any] = {"HTTP_HOST": "127.0.0.1"}
    if authed and token:
        extra["HTTP_AUTHORIZATION"] = "JWT " + token

    try:
        if method == "OPTIONS":
            extra.update(
                {
                    "HTTP_ORIGIN": "http://localhost:3000",
                    "HTTP_ACCESS_CONTROL_REQUEST_METHOD": "GET",
                    "HTTP_ACCESS_CONTROL_REQUEST_HEADERS": "authorization,content-type",
                }
            )
            resp = client.options(path, **extra)
        elif method == "GET":
            resp = client.get(path, **extra)
        elif method == "POST":
            resp = client.post(path, data=json.dumps({}), content_type="application/json", **extra)
        elif method == "PUT":
            resp = client.put(path, data=json.dumps({}), content_type="application/json", **extra)
        elif method == "PATCH":
            resp = client.patch(path, data=json.dumps({}), content_type="application/json", **extra)
        elif method == "DELETE":
            resp = client.delete(path, **extra)
        else:
            raise ValueError(method)
    except Exception as exc:
        return ProbeResult(
            path=path,
            method=method,
            authed=authed,
            status_code=599,
            cors_allow_origin=None,
            detail=str(exc)[:240],
        )

    allow_origin = resp.headers.get("Access-Control-Allow-Origin") if hasattr(resp, "headers") else None
    detail = ""
    try:
        payload = json.loads(resp.content.decode("utf-8"))
        if isinstance(payload, dict):
            if "detail" in payload:
                detail = str(payload.get("detail") or "")
            elif payload:
                detail = json.dumps(payload)[:240]
    except Exception:
        detail = ""
    return ProbeResult(path=path, method=method, authed=authed, status_code=int(resp.status_code), cors_allow_origin=allow_origin, detail=detail)


class Command(BaseCommand):
    def handle(self, *args, **options):
        paths = _iter_api_paths()
        token = _get_admin_token()
        client = Client()
        try:
            client.raise_request_exception = False
        except Exception:
            pass

        methods = ["OPTIONS", "GET"]
        results: list[ProbeResult] = []
        sink = io.StringIO()
        with redirect_stdout(sink), redirect_stderr(sink):
            for path in paths:
                for method in methods:
                    results.append(_probe(client, path, method, authed=False, token=None))
                    results.append(_probe(client, path, method, authed=True, token=token))

        failures_5xx = [r for r in results if 500 <= r.status_code <= 599]
        failures_4xx = [r for r in results if 400 <= r.status_code <= 499]
        cors_missing = [r for r in results if r.method == "OPTIONS" and not r.cors_allow_origin]

        report = {
            "summary": {
                "paths": len(paths),
                "probes": len(results),
                "failures_4xx": len(failures_4xx),
                "failures_5xx": len(failures_5xx),
                "cors_missing_on_options": len(cors_missing),
            },
            "failures_5xx": [r.__dict__ for r in failures_5xx[:200]],
            "failures_4xx": [r.__dict__ for r in failures_4xx[:400]],
            "cors_missing_on_options": [r.__dict__ for r in cors_missing[:200]],
        }

        self.stdout.write(json.dumps(report, indent=2))
