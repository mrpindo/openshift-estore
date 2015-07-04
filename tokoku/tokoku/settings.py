"""
Django settings for tokoku project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:    #Py3
    ON_OPENSHIFT = True

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))		#KO!, static dir files not resolved!
BASE_DIR = os.path.dirname(os.path.realpath(__file__))		#Works

if ON_OPENSHIFT:
    DEBUG = False	#False works on Openshift side :-)
else:
    DEBUG = True


TEMPLATE_DEBUG = DEBUG

#Django >= 1.5 specific
AUTH_USER_MODEL = 'myauth.MyUser'
#For signup
SIGNUP_EXPIRY_DAYS =  1

ADMINS = (
    ('Admin', 'admin@mrpindo.com'),
)


MANAGERS = ADMINS

#!! send_mail
if ON_OPENSHIFT:
#mail, production
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'admin@mrpindo.com'
    EMAIL_HOST_PASSWORD = 'secret'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

else:
#Following two methods are not to be use in production environment
##This procedure works! p
#mail, development
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret'

#only works when debug = false
ALLOWED_HOSTS = ['*']

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    #addded, endik Mar 9
    'django.core.context_processors.i18n',
    'tokoku.context_processors.ga_key',

    'django.contrib.messages.context_processors.messages',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myauth',
    'shop',
    'geo',
    'tokoku',
    'django.contrib.sites',
)


MIDDLEWARE_CLASSES = (
    #'tokoku.middleware.SSLRedirectMiddleware',		#This only works in Python3/CherryPy environment.
    #It seems this SSLRedirect/internal Django redirect not working
    #in Python3/Apache2 environment. Revert to .htaccess redirect

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tokoku.urls'

WSGI_APPLICATION = 'tokoku.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if ON_OPENSHIFT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'toko',
            'USER': 'admin',                      
            'PASSWORD': 'secret',                  
            'HOST': '',                      
            'PORT': '',                      
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', 
            'NAME': 'toko',
            #'USER': 'toko',             
            'USER': 'postgres',                      
            'PASSWORD': 'secret',                  
            'HOST': '',                      
            'PORT': '',                      
        }
    }

# Google Analytics
if ON_OPENSHIFT:
    GOOGLE_ANALYTICS_KEY = 'some key'
else:
    GOOGLE_ANALYTICS_KEY = ''

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'id'

_ = lambda s: s

LANGUAGES = (
    ('id', _('Bahasa Indonesia')),
    ('en', _('English')),
)

SITE_ID = 1

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Jakarta'


USE_I18N = True

USE_L10N = True

USE_TZ = True
# If you set this to False, Django will not use timezone-aware datetimes.
#USE_TZ = True    #set to false, by endik in order to facilitate xlwt
#USE_TZ = False

LOCALE_PATHS = (			#endik
    os.path.join(BASE_DIR, "locale"),
)

USE_THOUSAND_SEPARATOR = True		#endik

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
if ON_OPENSHIFT:
    MEDIA_ROOT = os.environ.get('OPENSHIFT_REPO_DIR', '')+'/wsgi/static/media'
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, '../..', 'static/media')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
if ON_OPENSHIFT:
    MEDIA_URL = '/static/media/'
else:
    MEDIA_URL = '/static/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
if ON_OPENSHIFT:
    STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/static/')
else:
    pass
    #STATIC_ROOT = os.path.join(BASE_DIR, '../..', 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
if ON_OPENSHIFT:
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        #os.path.join(BASE_DIR, '..', 'static'),
    )
else:
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(BASE_DIR, '../..', 'static'),
    )


