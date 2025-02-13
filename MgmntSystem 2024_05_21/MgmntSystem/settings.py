"""
Django settings for MgmntSystem project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ewg^zfi*7k=4(s7hhqko2z%ohu$o9*3ha89#se_=8)yb^w(&4s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['127.0.0.1', '10.2.12.92', 'localhost', 'ncr.sdmi.shi.co.jp', '10.2.14.15', '10.2.14.249', 'sdmi.shi.co.jp']
ALLOWED_HOSTS = ['ncrwepapptest.sdmi.shi.co.jp']


# Application definition


INSTALLED_APPS = [
    'NCRMgmntSystem.apps.NcrmgmntsystemConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    #'bootstrap_modal_forms',    
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

ROOT_URLCONF = 'MgmntSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
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

WSGI_APPLICATION = 'MgmntSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


#local database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'training_db',
#        'USER': 'sdmi',
#        'PASSWORD': 'sdmi',
#        'HOST': 'localhost',
#        'PORT': '3306'
#    }
#}

#DB for local test
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'ot',
#        'USER': 'otuser02',
#        'PASSWORD': 'otuser02',
#        'HOST': '10.2.1.18',
#        'PORT': '3306'
#    }
#}

#DB for acceptance test
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ot',
        'USER': 'sdmi',
        'PASSWORD': 'sdmi',
        'HOST': '10.2.1.166',
        'PORT': '3306'
    }
}

#overtime system test DB 2
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'ot',
#        'USER': 'otuser02',
#        'PASSWORD': 'otuser02',
#        'HOST': 'ncrwepapptest.sdmi.shi.co.jp',
#        'PORT': '3306'
#    }
#}

#production DB
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'ot',
#        'USER': 'sdmi',
#        'PASSWORD': 'sdmi',
#        'HOST': '10.2.1.147',
#        'PORT': '3306'
#    }
#}

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/



#Start modify Edric 2024/02/12 (I remove STATICFILES_DIRS from comment and put STATIC_ROOT to comment)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_URL = '/static/'

#STATIC_ROOT = os.path.join(BASE_DIR, "static")
#End modify Edric 2024/02/12




#DataFlair
#EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST = 'mx1.shi.co.jp'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'joseph.reginaldo@shi-g.com'
#EMAIL_HOST_USER = 'ji26842035@shi-g.com'
#EMAIL_HOST_PASSWORD = 'Gtfs373&'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_HOST = 'mx1.shi.co.jp'
EMAIL_PORT = 25

#CONTEXT_ROOT='/NCRMgmntSystem/'
CONTEXT_ROOT='/MgmntSystem/'
LOGIN_URL='/NCRMgmntSystem/login/'
LOGOUT_URL='/NCRMgmntSystem/logout/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



