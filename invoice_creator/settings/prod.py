from development.invoice_creator.invoice_creator.settings.dev import ALLOWED_HOSTS, SECRET_KEY
import django_on_heroku
from decouple import invoice_creator

from .base import *

SECRET_KEY = invoice_creater('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'django-invoice-creator.herokuapp.com',
	'business-invoice-creator.com'
]
