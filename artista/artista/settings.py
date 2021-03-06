"""
Django settings for artista project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
# import environ

# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )
# # reading .env file
# environ.Env.read_env()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oixxgi10byo%y)^l0a2f4omgidkvca!@#c=m*hiit^1qyv^1dh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


SITE_URL = 'http://127.0.0.1:8000/'
SITE_NAME = 'Artista'


# Application definition

INSTALLED_APPS = [
    ''
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.admindocs',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'sorl.thumbnail',
    # 'channels', #need asynchronous web server
    # 'chat',  #need asynchronous web server
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',

    'getstart',
    'login',
    'register',
    'forgotPass',
    'api',
    'dashboard',
    'artist',
    'client',
    'artistArt',
    'artistArtCategory',
    'artistFollowing',
]
INSTALLED_APPS += [
    "app_artInfo",
    'app_profileManagemant'
]


SITE_ID = 1


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.gzip.GZipMiddleware'
    # 'htmlmin.middleware.HtmlMinifyMiddleware',
    # 'htmlmin.middleware.MarkRequestMiddleware',

    # own Middleware
    'artista.middleware.MainMiddleware',
    'artista.middleware.CustomAuthMiddleware',
]

ROOT_URLCONF = 'artista.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'artista.wsgi.application'
# ASGI_APPLICATION = "artista.routing.application" # for asynchronous call  web server
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('redis-15871.c14.us-east-1-2.ec2.cloud.redislabs.com', 15871)],
#         },
#     },
# }

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 1,
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
}


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# SESSION files
SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_FILE_PATH = os.path.join(BASE_DIR, 'stroage/tmp/sessions/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/static/',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'stroage/media/upload/')
MEDIA_URL = "/media/upload/"

STATIC_URL = '/static/'


# Email Setup
# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_HOST_USER = '1d673a236e6229'
# EMAIL_HOST_PASSWORD = '96832748e4ec5f'
# EMAIL_PORT = '2525'

# Email Setup with file
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'stroage/tmp/emails/') # change this to a proper location
