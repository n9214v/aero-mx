import os
from django.contrib.messages import constants as messages

APP_CODE = 'AERO_MX'
APP_NAME = "Aero-MX"

# When no local_settings.py file exists, assume running in AWS
is_aws = not os.path.isfile('aero_mx/local_settings.py')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

DEBUG = False
ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$#9k_d0150y3nvkj5-=n1kfj1bj0#iw(e^jzfcy8*-(@005col'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # mjg_base
    'crequest',
    'sass_processor',
    'mjg_base',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    #
    'aero_mx',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aero_mx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['aero_mx/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',   # mjg_base
                'mjg_base.context_processors.util',
                'mjg_base.context_processors.auth',
            ],
            'libraries':{
                # If aero_mx had a taglib, it would need to be defined here:
                # 'aero_mx_taglib': 'aero_mx.templatetags.aero_mx_taglib',
            }
        },
    },
]


# https://django-allauth.readthedocs.io/en/latest/configuration.html
# -----------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1
SOCIALACCOUNT_PROVIDERS = {}
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = True

# -----------------------------------------------------------------------------

WSGI_APPLICATION = 'aero_mx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if is_aws:
    # AWS Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# For caching things (like database results)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Vancouver'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# SASS (https://github.com/jrief/django-sass-processor)
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'sass_build')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join('aero_mx', 'static', 'css'),
]
SASS_PROCESSOR_AUTO_INCLUDE = True  # App specific static folders are added to the libsass include dirs
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'
SASS_PRECISION = 8

SASS_PROCESSOR_CUSTOM_FUNCTIONS = {
    'get-color': 'mjg_base.services.template_service.get_sass_color',
    'get-string': 'mjg_base.services.template_service.get_sass_string',
}

# Message classes
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# GMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'n9214v@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'N9214V@gmail.com'


if (not is_aws) and (not os.path.isdir('logs')):
    os.mkdir('logs')


# Logging Settings
if is_aws:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': "[%(asctime)s] %(levelname)s %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'WARN',
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'aero_mx': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        }
    }
else:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': "[%(asctime)s] %(levelname)s %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'logs/aero_mx.log',
                'formatter': 'standard'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'file'],
                'propagate': True,
                'level': 'WARN',
            },
            'django.db.backends': {
                'handlers': ['console', 'file'],
                'level': 'ERROR',
                'propagate': False,
            },
            'aero_mx': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
            },
        }
    }

# Get SASS Variables
if os.path.isfile('aero_mx/sass_variables.py'):
    from .sass_variables import *

# Session expiration
SESSION_COOKIE_AGE = 30 * 60  # 30 minutes

# In AWS (Elastic Beanstalk), values will be in environment variables
if is_aws:
    HOST_NAME = os.environ.get('HOST_NAME', 'localhost')
    HOST_IP = os.environ.get('HOST_IP')
    HOST_URL = os.environ.get('HOST_URL')

    # Do not attempt to compile SASS in AWS (permission errors)
    SASS_PROCESSOR_ENABLED = False

    # https://docs.djangoproject.com/en/2.2/topics/security/#ssl-https
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # https://docs.djangoproject.com/en/2.2/ref/middleware/#http-strict-transport-security
    # SECURE_HSTS_SECONDS = 31536000  # One Year

    ALLOWED_HOSTS = ['*', 'localhost', HOST_NAME, HOST_IP, HOST_URL]
    ENVIRONMENT = os.environ.get('ENVIRONMENT', 'DEV')
    DEBUG = str(os.environ.get('DEBUG', 'False')).lower() == 'true'
    SECRET_KEY = os.environ.get('SECRET_KEY', None)

# Otherwise, override settings with values from local_settings.py
else:
    from .local_settings import *
