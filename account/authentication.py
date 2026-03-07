# account/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return None
        request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'
        return super().authenticate(request)

    def authenticate_header(self, request):
        return None


class QuietJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        auth = request.META.get("HTTP_AUTHORIZATION")
        if isinstance(auth, str) and auth.startswith("JWT "):
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {auth[4:].strip()}"
        return super().authenticate(request)

    def authenticate_header(self, request):
        return None
