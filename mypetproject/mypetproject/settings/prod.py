from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_laiwds!+venxmt#bd3nmw5o1g@rg$i6+^$1)xo80(squz@#-l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SITE_ID = 1

ALLOWED_HOSTS = [
  '*',
  'localhost',
  '127.0.0.1',
  '111.222.333.444',
  'mywebsite.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'buyit_store',
        'USER' : 'admin',
        'PASSWORD' : 'qwerty',
        'HOST' : 'db',
        'PORT' : '5432',
    }
}
