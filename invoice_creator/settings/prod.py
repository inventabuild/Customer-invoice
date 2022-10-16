from development.invoice_creator.invoice_creator.settings.dev import ALLOWED_HOSTS, SECRET_KEY
import django_on_heroku
from decouple import invoice_creator

from .base import *

SECRET_KEY = invoice_creator('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'django-invoice-creator.herokuapp.com',
	'business-invoice-creator.com',
]

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'verbose': {
            'format' : "[%(asctime}s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

# Heroku Settings
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']
