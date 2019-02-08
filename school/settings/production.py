from .base import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600  # FIXME: increase when site is ready
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_env_variable("DJANGO_DB_NAME"),
        "USER": get_env_variable("DJANGO_DB_USER"),
        "PASSWORD": get_env_variable("DJANGO_DB_PASSWORD"),
        "HOST": get_env_variable("DJANGO_DB_HOST"),
        "PORT": get_env_variable("DJANGO_DB_PORT"),
    }
}

ALLOWED_HOSTS = [
    get_env_variable("SERVER_DOMAIN"),
    get_env_variable("SERVER_IP"),
    "localhost",
]

sentry_sdk.init(dsn=get_env_variable("SENTRY_LINK"), integrations=[DjangoIntegration()])

EMAIL_HOST = get_env_variable("EMAIL_HOST")
EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD")
EMAIL_PORT = get_env_variable("EMAIL_PORT")
EMAIL_USE_TLS = get_env_variable("EMAIL_USE_TLS")
