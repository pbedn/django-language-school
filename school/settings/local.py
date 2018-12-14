from .base import *

SECRET_KEY = 'secret_key'

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

HOST = 'http://127.0.0.1:8000'

AUTH_PASSWORD_VALIDATORS = []

INSTALLED_APPS += ['django-extensions', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'school',
        'USER': 'school',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '',
    }
}
