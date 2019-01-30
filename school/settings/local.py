from .base import *

SECRET_KEY = "secret_key"

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

HOST = "http://127.0.0.1:8000"

AUTH_PASSWORD_VALIDATORS = []

INSTALLED_APPS += ["django_extensions"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        # need to use str here a sit would not be fixed until Python 3.8
        # FUTURE: Remove str
        "NAME": str(PROJECT_DIR / "school.db"),
    }
}
