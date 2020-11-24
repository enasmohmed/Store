import os
from .settings import *

import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['djangonewapp.herokuapp.com']

DATABASES_URL = os.environ.get('DATABASES_URL')


DATABASES = {
    'default': dj_database_url.config(os.environ.get('DATABASES_URL'))
}