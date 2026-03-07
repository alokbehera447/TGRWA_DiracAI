# CORS/CORB + PATCH fix: /api/employee-documents/<id>/

## Symptoms

- Browser shows CORB/CORS errors when calling:
  - `PATCH http://127.0.0.1:8000/api/employee-documents/1/`
- Server logs show `415 Unsupported Media Type` or `400 Bad Request`.
- Unauthenticated calls show `WWW-Authenticate` header (unwanted).

## Root causes

1) **415 Unsupported Media Type**
- The endpoint only accepted multipart/form-data at first.
- Frontend sent JSON (`Content-Type: application/json`) for PATCH.

2) **400 Bad Request**
- Frontend sent `file: null` or `file: ""` during PATCH, causing file validation errors.
- Frontend sent status values like `Active` (not matching model choices `pending|approved|rejected`).

3) **CORB/CORS**
- CORB typically appears when the browser blocks reading the response due to missing CORS headers or wrong/HTML responses.
- Fixes ensure:
  - CORS headers are present on both success and error responses.
  - Responses are always JSON for these endpoints.

## Server-side fixes (required)

### A) Suppress WWW-Authenticate header
Use `QuietJWTAuthentication` for the employee document endpoints so 401/403 responses do not add the `WWW-Authenticate` challenge header.

### B) Accept both JSON and multipart for PATCH
Enable `JSONParser` alongside `MultiPartParser` and `FormParser`.

### C) Avoid file=null validation errors
Ignore `"file": null` / `"file": ""` during PATCH (do not try to overwrite the file).

### D) Normalize admin status inputs
Map common values to model choices:
- `active|accepted|approve` → `approved`
- `inactive|declined|reject` → `rejected`

### E) Always return JSON (avoid CORB/HTML renderer)
Set `renderer_classes = [JSONRenderer]` for employee document list/detail endpoints.

## CORS requirements (Django settings)

Ensure:
- `corsheaders` is in `INSTALLED_APPS`
- Middleware order includes `CorsMiddleware` before `CommonMiddleware`
- CORS settings allow your frontend origin(s)

Example working dev config:

```python
INSTALLED_APPS += ["corsheaders"]

MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "corsheaders.middleware.CorsMiddleware",
  "django.middleware.common.CommonMiddleware",
  ...
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
```

## Client-side rules (required)

### If you are updating only text/status fields
Send JSON:
- `Content-Type: application/json`

### If you are updating the file
Send multipart/form-data:
- Use `FormData`
- **Do not** manually set `Content-Type` (browser must set boundary)

### Do not send `file: null`
Only send `file` when a real file is selected.

## Testing scripts

### 1) Preflight (OPTIONS)
This must return 200 and include allow headers/methods:

```bash
curl.exe -i -X OPTIONS "http://127.0.0.1:8000/api/employee-documents/1/" ^
  -H "Origin: http://localhost:3000" ^
  -H "Access-Control-Request-Method: PATCH" ^
  -H "Access-Control-Request-Headers: authorization,content-type"
```

Expected headers include:
- `Access-Control-Allow-Origin: http://localhost:3000`
- `Access-Control-Allow-Methods` includes `PATCH`
- `Access-Control-Allow-Headers` includes `authorization, content-type`
- `Vary: Origin`

### 2) Get admin token (PowerShell)

```powershell
$body = @{ username="admin"; password="YOUR_ADMIN_PASSWORD" } | ConvertTo-Json
$tok = Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/api/token/" -ContentType "application/json" -Body $body
$tok.access
```

### 3) PATCH (JSON) – should return 200

```powershell
$token = $tok.access
$headers = @{ Authorization = "JWT $token"; Origin = "http://localhost:3000" }
$payload = @{ status = "Active" } | ConvertTo-Json

Invoke-RestMethod -Method Patch -Uri "http://127.0.0.1:8000/api/employee-documents/1/" `
  -Headers $headers -ContentType "application/json" -Body $payload
```

Expected:
- HTTP 200
- Response `Content-Type: application/json`
- No `WWW-Authenticate` header
- Has `Access-Control-Allow-Origin: http://localhost:3000`

### 4) PATCH (multipart) – update file

```powershell
$token = $tok.access
$headers = @{ Authorization = "JWT $token"; Origin = "http://localhost:3000" }

$form = @{
  document_type = "Resume"
  title = "Updated resume"
  file = Get-Item "C:\\path\\to\\resume.pdf"
}

Invoke-RestMethod -Method Patch -Uri "http://127.0.0.1:8000/api/employee-documents/1/" `
  -Headers $headers -Form $form
```

## Referrer policy note

`strict-origin-when-cross-origin` only affects the `Referer` header the browser sends. It does not block CORS by itself. The above tests validate behavior using the `Origin` header, which is what CORS relies on.

