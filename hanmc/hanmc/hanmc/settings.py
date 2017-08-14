# -*- coding: utf-8 -*-
"""
Django settings for hanmc project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rxgcneizo6r^f40gs^+#hp_wj0%sg&n0$+grvod(@_*&jll97%'

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
    'polls',
    'faceunlock',
    'home',
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

ROOT_URLCONF = 'hanmc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'hanmc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hanmc',
        'USER': 'root',   
        'PASSWORD': 'root',   
        'HOST': '127.0.0.1',   
        'PORT': '3306',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'



'''更换Users模型
# Users register
AUTH_USER_MODEL = 'users.User'

#要求认证邮箱以激活账号
# USERS_VERIFY_EMAIL = True
# USERS_AUTO_LOGIN_ON_ACTIVATION = True
# USERS_EMAIL_CONFIRMATION_TIMEOUT_DAYS = 3

#认证邮件发送方设置,使用企业邮箱比较容易。还是没有成功，暂时关掉邮箱认证。
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = False
# EMAIL_HOST = 'smtp.hanmengcheng.com'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = 'hanmc@hanmengcheng.com'
# EMAIL_HOST_PASSWORD = 'Han8528520258'
# DEFAULT_FROM_EMAIL = 'hanmc@tuweizhong.com'

#开放用户注册
USERS_REGISTRATION_OPEN = True
USERS_PASSWORD_MIN_LENGTH = 5
USERS_PASSWORD_MAX_LENGTH = None
USERS_CHECK_PASSWORD_COMPLEXITY = True
USERS_SPAM_PROTECTION = True
USERS_PASSWORD_POLICY = {
        'UPPER': 0,       # Uppercase 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        'LOWER': 0,       # Lowercase 'abcdefghijklmnopqrstuvwxyz'
        'DIGITS': 0,      # Digits '0123456789'
        'PUNCTUATION': 0  # Punctuation """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
}

#superuser
USERS_CREATE_SUPERUSER = DEBUG
USERS_SUPERUSER_EMAIL = 'feifanhanmc@163.com'
USERS_SUPERUSER_PASSWORD = 'han8528520258'
'''