from .base import *

SECRET_KEY = 'secret_key'

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

HOST = 'http://127.0.0.1:8000'

AUTH_PASSWORD_VALIDATORS = []

INSTALLED_APPS += ['django_extensions', ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
