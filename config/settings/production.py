"""
Production settings.
"""

from .base import *  # noqa: F403

DEBUG = False

ALLOWED_HOSTS = ['maine-maps-cms.digitalgizmo.com']

CORS_ALLOWED_ORIGINS = [
    'https://dev.digitalgizmo.com',
]

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600  # 1 hour — increase to 31536000 once SSL is confirmed stable
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Enable when ready
# SECURE_HSTS_PRELOAD = True  # Enable only after stable — this is very hard to undo

STATIC_ROOT = BASE_DIR / 'static'  # noqa: F405
