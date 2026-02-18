"""
Production settings.
"""

from .base import *  # noqa: F403

DEBUG = False

ALLOWED_HOSTS = ['maine-maps-cms.digitalgizmo.com']

CORS_ALLOWED_ORIGINS = [
    # Add your production frontend origin here, e.g.:
    # 'https://dev.digitalgizmo.com',
]

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

STATIC_ROOT = BASE_DIR / 'static'  # noqa: F405
