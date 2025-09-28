from jacco.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-kk+!i=8=*uj(n%jv4@ka0#1#l&qzj0*t@@o6fei46_83rh-jab'

DEBUG = False


ALLOWED_HOSTS = [
    "jambocongo.com",
    "www.jambocongo.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://jambocongo.com",
    "https://www.jambocongo.com",
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jacco_db',
        'USER': 'jacco_user',
        'PASSWORD': 'jacco_pass',
        'HOST': 'jacco_prod_app_pgsql',
        'PORT': '5432',
    }
}