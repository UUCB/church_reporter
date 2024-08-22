from .base import *
import environ

env = environ.Env(
    REPORTER_DEBUG=(bool, False),
    REPORTER_ALLOWED_HOSTS=(list, []),
)


SECRET_KEY = env('REPORTER_SECRET_KEY')

DEBUG = env('REPORTER_DEBUG')

ALLOWED_HOSTS = env('REPORTER_ALLOWED_HOSTS')
CSRF_TRUSTED_ORIGINS = ['https://' + host for host in ALLOWED_HOSTS]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / env('REPORTER_SQLITE3_PATH'),
    }
}

STATIC_ROOT = env('REPORTER_STATIC_ROOT')

MEDIA_ROOT = env('REPORTER_MEDIA_ROOT')
MEDIA_URL = '/media/'
