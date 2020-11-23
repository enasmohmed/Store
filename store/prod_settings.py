import os
from .settings import *


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['serene-peak-87406.herokuapp.com']