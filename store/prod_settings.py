import os
from .settings import *

import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')


DEBUG = True

ALLOWED_HOSTS = ['djangonewapp.herokuapp.com']

DATABASES_URL = os.environ.get('DATABASES_URL')


DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASES_URL'))
}


# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

