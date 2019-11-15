"""
Django settings for afrh_prj project.
"""

import os
import arches
import inspect

try:
    from arches.settings import *
except ImportError:
    pass

APP_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
STATICFILES_DIRS =  (os.path.join(APP_ROOT, 'media'),) + STATICFILES_DIRS

DATATYPE_LOCATIONS.append('afrh_prj.datatypes')
FUNCTION_LOCATIONS.append('afrh_prj.functions')
SEARCH_COMPONENT_LOCATIONS.append('afrh_prj.search_components')
TEMPLATES[0]['DIRS'].append(os.path.join(APP_ROOT, 'functions', 'templates'))
TEMPLATES[0]['DIRS'].append(os.path.join(APP_ROOT, 'widgets', 'templates'))
TEMPLATES[0]['DIRS'].insert(0, os.path.join(APP_ROOT, 'templates'))

LOCALE_PATHS.append(os.path.join(APP_ROOT, 'locale'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xxxx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ROOT_URLCONF = 'afrh_prj.urls'

# a prefix to append to all elasticsearch indexes, note: must be lower case
ELASTICSEARCH_PREFIX = 'afrh_prj'

ELASTICSEARCH_CUSTOM_INDEXES = []
# [{
#     'module': 'afrh_prj.search_indexes.sample_index.SampleIndex',
#     'name': 'my_new_custom_index' <-- follow ES index naming rules
# }]

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",
        "NAME": "afrh_prj",
        "OPTIONS": {},
        "PASSWORD": "xxxx",
        "PORT": "5432",
        "POSTGIS_TEMPLATE": "template_postgis",
        "TEST": {
            "CHARSET": None,
            "COLLATION": None,
            "MIRROR": None,
            "NAME": None
        },
        "TIME_ZONE": None,
        "USER": "postgres"
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'arches',
    'arches.app.models',
    'arches.management',
    'guardian',
    'captcha',
    'revproxy',
    'corsheaders',
    'oauth2_provider',
    'django_celery_results',
    'afrh_prj',
)

ALLOWED_HOSTS = ["*"]

SYSTEM_SETTINGS_LOCAL_PATH = os.path.join(APP_ROOT, 'system_settings', 'System_Settings.json')
WSGI_APPLICATION = 'afrh_prj.wsgi.application'
STATIC_ROOT = '/var/www/media'

RESOURCE_IMPORT_LOG = os.path.join(APP_ROOT, 'logs', 'resource_import.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',  # DEBUG, INFO, WARNING, ERROR
            'class': 'logging.FileHandler',
            'filename': os.path.join(APP_ROOT, 'arches.log'),
            'formatter': 'console'
        },
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        }
    },
    'loggers': {
        'arches': {
            'handlers': ['file', 'console'],
            'level': 'WARNING',
            'propagate': True
        }
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT =  os.path.join(APP_ROOT)

# Sets default max upload size to 15MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640

# Unique session cookie ensures that logins are treated separately for each app
SESSION_COOKIE_NAME = 'afrh_prj'

CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    #     'LOCATION': os.path.join(APP_ROOT, 'tmp', 'djangocache'),
    #     'OPTIONS': {
    #         'MAX_ENTRIES': 1000
    #     }
    # }
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

#Identify the usernames and duration (seconds) for which you want to cache the time wheel
CACHE_BY_USER = {'anonymous': 3600 * 24}

MOBILE_OAUTH_CLIENT_ID = ''  #'9JCibwrWQ4hwuGn5fu2u1oRZSs9V6gK8Vu8hpRC4'
MOBILE_DEFAULT_ONLINE_BASEMAP = {'default': 'mapbox://styles/mapbox/streets-v9'}

APP_TITLE = 'Arches | Heritage Data Management'
COPYRIGHT_TEXT = 'All Rights Reserved.'
COPYRIGHT_YEAR = '2019'

CELERY_BROKER_URL = 'amqp://guest:guest@localhost'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'django-db' # Use 'django-cache' if you want to use your cache as your backend
CELERY_TASK_SERIALIZER = 'json'

try:
    from .package_settings import *
except ImportError:
    pass

try:
    from .settings_local import *
except ImportError:
    pass
