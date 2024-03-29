"""
Django settings for afrh_iris project.
"""

import os
import inspect

try:
    from arches.settings import *
except ImportError:
    pass

APP_NAME = 'AFRH IRIS'
APP_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
DOCS_ROOT = os.path.join(os.path.dirname(APP_ROOT), ".docs")
STATICFILES_DIRS =  (
    os.path.join(APP_ROOT, 'media'),
    os.path.join(DOCS_ROOT, "assets")
) + STATICFILES_DIRS

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
ELASTICSEARCH_PREFIX = 'afrh_iris'

ELASTICSEARCH_CUSTOM_INDEXES = []
# [{
#     'module': 'afrh_iris.search_indexes.sample_index.SampleIndex',
#     'name': 'my_new_custom_index' <-- follow ES index naming rules
# }]

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",
        "NAME": "noname",
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

INSTALLED_APPS += (
    'afrh_prj',
    'iris',
)

ALLOWED_HOSTS = ["*"]

ARCHES_NAMESPACE_FOR_DATA_EXPORT = "http://afrh-iris.com/"

HIDE_EMPTY_NODES_IN_REPORT = True

ENABLE_USER_SIGNUP = False

SYSTEM_SETTINGS_LOCAL_PATH = os.path.join(APP_ROOT, 'system_settings', 'System_Settings.json')
WSGI_APPLICATION = 'afrh_prj.wsgi.application'

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
SESSION_COOKIE_NAME = 'afrh_iris'

#Identify the usernames and duration (seconds) for which you want to cache the time wheel
CACHE_BY_USER = {'anonymous': 3600 * 24}

MOBILE_OAUTH_CLIENT_ID = ''  #'9JCibwrWQ4hwuGn5fu2u1oRZSs9V6gK8Vu8hpRC4'
MOBILE_DEFAULT_ONLINE_BASEMAP = {'default': 'mapbox://styles/mapbox/streets-v9'}

APP_TITLE = 'AFRH-IRIS'
APP_NAME = APP_TITLE
COPYRIGHT_TEXT = 'All Rights Reserved.'
COPYRIGHT_YEAR = '2022'

CELERY_BROKER_URL = 'amqp://guest:guest@localhost'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'django-db' # Use 'django-cache' if you want to use your cache as your backend
CELERY_TASK_SERIALIZER = 'json'

try:
    from .settings_local import *
except ImportError:
    pass
