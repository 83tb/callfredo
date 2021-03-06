import os
import dj_database_url

SITE_ROOT = os.path.join(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!2g!w2h4mm=67b@)=snbf-ptv0*j9a6b+c2ze=2s3&amp;q86der&amp;e'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonehome',
    'django.contrib.admin',
    'south',
    'social_auth',
    'accounts',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# Auth settings
CUSTOM_USER_MODEL = 'accounts.User'
SOCIAL_AUTH_USER_MODEL = CUSTOM_USER_MODEL

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'accounts.backends.UserModelBackend',
)

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook',)

LOGIN_REDIRECT_URL = '/givenumber/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/givenumber/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/givenumber/'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/accounts/social-error/'

# Facebook perms
FACEBOOK_EXTENDED_PERMISSIONS = ['friends_birthday','publish_stream']

FACEBOOK_APP_ID = '420588444667164'
FACEBOOK_API_SECRET = '953cac899ca6f17b400191cd071e3b66'

# Twilio

#konto Marka
#ACCOUNT_SID = 'ACd9069181b7ebff5c6fe8d62d6ee8b15e'
#AUTH_TOKEN = '4e0d3996074d07b5d9a42be566e4161f'
#OUTGOING_NUMBER = '+48128810896'

#konto Kuby
ACCOUNT_SID = 'AC782ab20af29cb4bc1be863601e54f1e1'
AUTH_TOKEN = '547518f3e6116718819e8208a129f328'
OUTGOING_NUMBER = '6503186255';


# Soundcloud
SOUNDCLOUD_CLIENT_ID = '166a8139b54baa4eadd270f578ee19f8'
SOUNDCLOUD_CLIENT_SECRET = 'd82089dd3ca94c3459f195386ce9eb43'
SOUNDCLOUD_USERNAME = 'callfredo'
SOUNDCLOUD_PASSWORD = 'fredo1324'


try:
    from localsettings import *
except ImportError:
    pass
