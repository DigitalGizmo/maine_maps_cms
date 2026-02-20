"""
Local development settings.
"""

from .base import *  # noqa: F403

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

STATIC_ROOT = BASE_DIR / 'static'  # noqa: F405

# CORS — allow Vite dev server
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://localhost:5174',
]
