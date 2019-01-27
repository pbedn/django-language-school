from .base import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DJANGO_DB_NAME'),
        'USER': get_env_variable('DJANGO_DB_USER'),
        'PASSWORD': get_env_variable('DJANGO_DB_PASSWORD'),
        'HOST': get_env_variable('DJANGO_DB_HOST'),
        'PORT': get_env_variable('DJANGO_DB_PORT'),
    }
}

ALLOWED_HOSTS = [get_env_variable('SERVER_DOMAIN'),
                 get_env_variable('SERVER_IP'),
                 'localhost']

sentry_sdk.init(
    dsn=get_env_variable('SENTRY_LINK'),
    integrations=[DjangoIntegration()]
)
