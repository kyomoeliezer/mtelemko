"""
Django settings for mtelemko project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/s
"""

import os
#import pymysql

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),

)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$!#-o07(@73ga1401apy=bif#ecwk7q2^$y794$%k!ix&g+dw*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SECURE_SSL_REDIRECT=False
# Application definition

INSTALLED_APPS = [
    'product.apps.ProductConfig',
    'meeting.apps.MeetingConfig',
    'user.apps.UserConfig',
    'contact.apps.ContactConfig',
    'lead.apps.LeadConfig',
    'tender.apps.TenderConfig',
    'project.apps.ProjectConfig',
    'common.apps.CommonConfig',
    'invoice.apps.InvoiceConfig',
    'payment.apps.PaymentConfig',
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'crispy_forms',
    'import_export',
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

ROOT_URLCONF = 'mtelemko.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
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
#SESSION
#SESSION_EXPIRE_AT_BROWSER_CLOSE = False
#SESSION_COOKIE_AGE = 5 * 60 #
###
WSGI_APPLICATION = 'mtelemko.wsgi.application'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
###
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'premium54.web-hosting.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'm-sales@mifumotz.com'
EMAIL_HOST_PASSWORD = '.uSY~.t,1sU='
#DEFAULT_FROM_EMAIL  = 'ab@mifumotz.com'
#EMAIL_HOST_USER = 'absoftware@mifumotz.com'
#EMAIL_HOST_PASSWORD = '=3llT7LjdRPI'
DEFAULT_FROM_EMAIL  = 'm-sales@mifumotz.com'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
"""
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite_live24nov2020'),
   }
}
""" 
DATABASES = {
    'default': {
        'NAME': 'mifubfzr_msales',
        ##'NAME':'msalesj2023',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mifubfzr_msales',
        ##'USER':'root',
        ##'PASSWORD':'',
        'PASSWORD': 'mifumotz_msales',
        'HOST':'localhost',
        'OPTIONS': {
            'autocommit': True,
            "init_command": "SET storage_engine=MYISAM",
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


""""""
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True
IMPORT_EXPORT_USE_TRANSACTIONS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#####LOCAL HOST
"""
STATIC_URL = '/static/'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
STATICFILES_DIRS = (
  os.path.join(BASE_DIR , 'static'),
)
"""
STATIC_URL = 'http://m-sales.mifumotz.com/static/'
STATIC_ROOT = "/home/mifubfzr/m-sales.mifumotz.com/static/"


MEDIA_ROOT = "/home/mifubfzr/m-sales.mifumotz.com/media/"
MEDIA_URL = 'http://m-sales.mifumotz.com/media/'


IMPORT_EXPORT_USE_TRANSACTIONS = True

AUTH_USER_MODEL = 'user.User'


INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
#####SESSION EXPIRE
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_COOKIE_AGE = 1800 # set just 2hours
#SESSION_SAVE_EVERY_REQUEST = False
