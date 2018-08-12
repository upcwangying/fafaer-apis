"""
Django settings for fafaerapis project.

Generated by 'django-admin startproject' using Django 1.11.15.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(0, os.path.join(BASE_DIR, "extra_apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6h2c+3=s7s!j@@1)dnx(wttq@qn4i$d1b(nxyw)6yb6@3=-!^j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'xadmin',
    'crispy_forms',
    'django_oss_storage',
    'rest_framework',
    'rest_framework.authtoken',
    'users.apps.UsersConfig',
    'mp.apps.MpConfig',
    'music.apps.MusicConfig',
    'videos.apps.VideosConfig',
    'photos.apps.PhotosConfig'
]

AUTH_USER_MODEL = "users.User"

# Application definition
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fafaerapis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'fafaerapis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fafaerapis',
        'USER': 'root',
        'PASSWORD': 'Pa55Word',
        'HOST': '127.0.0.1',
        # 'OPTIONS': {'init_command': 'SET storage_engine=INNODB;'}
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB;'}
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'django_oss_storage.backends.OssStaticStorage'
DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'

OSS_ACCESS_KEY_ID = 'LTAIzh4ZeURSvNKz'
OSS_ACCESS_KEY_SECRET = 'Gqk7nfN7JoYPMZDGa9UwDK27wANLQv'
OSS_BUCKET_NAME = 'fafaer'
OSS_ENDPOINT = 'cdn.chenyifaer.com'


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    )
}


JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

# 图片文件上传设置
# 默认为10MB
IMAGE_UPLOAD_MAX_SIZE = 10 * 1024 * 1024
IMAGE_UPLOAD_TYPE = [
    'jpg',
    'png'
]

# 音乐文件上传设置
# 默认为15MB
MUSIC_UPLOAD_MAX_SIZE = 15 * 1024 * 1024
MUSIC_UPLOAD_TYPE = [
    'mp3',
    # 'png'
]

# 音乐文件上传设置
# 默认为150MB
VIDEO_UPLOAD_MAX_SIZE = 150 * 1024 * 1024
VIDEO_UPLOAD_TYPE = [
    'mp4',
    # 'png'
]