"""
Django settings for WhereTheMove project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '636q_i+l==^#dvv#pd8s3i@8t_ns%zjq(riqozv=7*52)@5)7a'
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
     'whats-the-moove.herokuapp.com','localhost'
]


# Application definition

INSTALLED_APPS = [
    #local
    'Events.apps.EventsConfig',
    'users.apps.UsersConfig',
    'api.apps.ApiConfig',
    #default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'django_comments_xtd',
    'django_comments',

    #third party
    'crispy_forms',
    'django_cleanup',
    'tinymce',
    "mapbox_location_field",
    'social_django',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'rest_auth',
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_auth.registration",
    'storages',
]

#api
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'api.permissions.APIRequestAuthentication'
        ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' ,
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',  # <--
]

ROOT_URLCONF = 'WhereTheMove.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'WhereTheMove.wsgi.application'


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
AUTHENTICATION_BACKENDS = (
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
# 'django.contrib.staticfiles.storage.StaticFilesStorage'
# STATICFILES_STORAGE = 'WhereTheMove.storage.WhiteNoiseStaticFilesStorage'

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MAPBOX_KEY = os.environ.get("MAPBOX_API_KEY")

LOGIN_REDIRECT_URL = 'explore' 
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
default_map_attrs = {
            "style": "mapbox://styles/mapbox/outdoors-v11",
            "zoom": 13,
            "center": [17.031645, 51.106715],
            "cursor_style": 'pointer',
            "marker_color": "red",
            "rotate": False,
            "geocoder": True,
            "fullscreen_button": True,
            "navigation_buttons": True,
            "track_location_button": True,
            "readonly": True,
            "placeholder": "Pick a location on map below",
        }

SITE_ID = 1
# social auth

SOCIAL_AUTH_GITHUB_KEY=os.environ.get("SOCIAL_AUTH_GITHUB_KEY")
SOCIAL_AUTH_GITHUB_SECRET=os.environ.get("SOCIAL_AUTH_GITHUB_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GITHUB_SECRET=os.environ.get("SOCIAL_AUTH_GITHUB_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
SOCIAL_AUTH_FACEBOOK_KEY=os.environ.get("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET=os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET")
SOCIAL_AUTH_TWITTER_KEY=os.environ.get("SOCIAL_AUTH_TWITTER_KEY")
SOCIAL_AUTH_TWITTER_SECRET=os.environ.get("SOCIAL_AUTH_TWITTER_SECRET")
# TOKEN = "AAAAAAAAAAAAAAAAAAAAAMB0IQEAAAAAOFz4qeGhzrbdLzadvDPsDFthc6Y%3D5OVDij6P0gbqudV3w8gfgCBjuk3bpsvC2xcSUMNyL8QIqWkbVC"


#send email 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT =587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "Helpdesk <helpdesk@whatsthemove>"


#comments
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MODEL = 'Events.models.Comments'
COMMENTS_XTD_SALT = (b"Timendi causa est nescire. "
                     b"Aequam memento rebus in arduis servare mentem.")
COMMENTS_XTD_FROM_EMAIL = "noreply@whatsthemove.com"
COMMENTS_XTD_CONTACT_EMAIL = "helpdesk@whatsthemove.com"
COMMENTS_XTD_MAX_THREAD_LEVEL = 2  # default is 0
COMMENTS_XTD_LIST_ORDER = ('-thread_id', 'order') 
COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'default': {
        'allow_flagging': False,
        'allow_feedback': True,
        'show_feedback': True,
        'who_can_post': 'user'  # Valid values: 'all', users'
    }
}

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET")
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME='us-east-2'

django_heroku.settings(locals())