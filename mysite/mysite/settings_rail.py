from mysite.settings import *
from decouple import config
SECRET_KEY=config('SECRET_KEY')

ALLOWED_HOSTS = ['calorietracker-production.up.railway.app']

CSRF_TRUSTED_ORIGINS = ['https://calorietracker-production.up.railway.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
        'OPTIONS': {'sslmode':'require'},
    }
}

import os
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'shop/static')]
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"