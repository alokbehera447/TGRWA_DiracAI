# Production settings for DiracAI deployment
from .settings import *

# SECURITY SETTINGS
DEBUG = False

ALLOWED_HOSTS = [
    'diracai.com',
    'www.diracai.com',
    '159.89.160.157',  # Your server IP
    'localhost',
    '127.0.0.1'
]

# CORS Configuration for Next.js frontend
CORS_ALLOWED_ORIGINS = [
    'https://diracai.com',
    'https://www.diracai.com',
    'http://localhost:3000',  # For local Next.js development
]

CORS_ALLOW_CREDENTIALS = True

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    'https://diracai.com',
    'https://www.diracai.com',
]

# Database - Keep PostgreSQL for production
DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'myproject', 
        'USER': 'diracai', 
        'PASSWORD': 'diracai', 
        'HOST': 'localhost', 
        'PORT': '5432', 
    } 
}

# Static and Media files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Use AWS S3 for production file storage (as configured)
# ALWAYS_UPLOAD_FILES_TO_AWS is already True in settings.py

print("🚀 Using PRODUCTION settings for DiracAI")


