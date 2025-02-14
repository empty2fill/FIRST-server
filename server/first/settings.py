"""
Django settings for first project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import json

#   Read in configuration data
FIRST_CONFIG_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                '..',
                                'first_config.json')
CONFIG = {}
try:
    with open(FIRST_CONFIG_FILE, "r") as f:
        config_data = json.load(f)
    if type(config_data) == dict:
        CONFIG = config_data
except IOError as ioe:
    print('[1st] IOError: {}'.format(ioe))
except ValueError as ve:
    print('[1st] ValueError: {}'.format(ve))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get('secret_key',
                        'd2nev@620*3vi@qvynch)seb4^pghp=-)aenfs(4%)-k@xqpo9')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = CONFIG.get('debug', True)

ALLOWED_HOSTS = CONFIG.get('allowed_hosts', [])


# Application definition

INSTALLED_APPS = [
    'www.apps.WwwConfig',
    'engines.apps.EnginesConfig',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'first.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'www', 'templates'),
            os.path.join(BASE_DIR, 'rest', 'templates'),
        ],
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

WSGI_APPLICATION = 'first.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': CONFIG.get('db_engine', 'django.db.backends.mysql'),
        'NAME': CONFIG.get('db_dbname', 'first_db'),
        'USER': CONFIG.get('db_user', 'root'),
        'PASSWORD': CONFIG.get('db_password', ''),
        'HOST': CONFIG.get('db_host', 'localhost'),
        'PORT': CONFIG.get('db_port', 3306)
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = CONFIG.get('language_code', 'en-us')

TIME_ZONE = CONFIG.get('time_zone', 'EST')

USE_I18N = CONFIG.get('use_i18n', True)

USE_L10N = CONFIG.get('use_l10n', True)

USE_TZ = CONFIG.get('use_tz', True)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'www/static')

STATIC_URL = CONFIG.get('static_url', '/static/')
