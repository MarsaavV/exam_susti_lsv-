from .base import

SECRET_KEY = 'django-insecure-g#yt!m)b!3s8*oj#z0t=pv=2$104y49+bhtb^$bpe5fo&v1!3f'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Configuración en base.py o local.py
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bd_restaurant_app_LSV',
        'USER': 'postgres',
        'PASSWORD': 'lima2006',
        'HOST': 'localhost',
        'PORT':'5432'
    }
}

STATIC_URL = 'static/'
