from .base import *

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
