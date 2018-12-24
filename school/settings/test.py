from .base import *

SECRET_KEY = 'secret_key'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # need to use str here a sit would not be fixed until Python 3.8
        # FUTURE: Remove str
        'NAME': str(PROJECT_DIR / 'test.db'),
    }
}
