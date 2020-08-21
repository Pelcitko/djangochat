import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '9nneu#^7_aai*(#(6_qiihu-^k-+%a86&vjh=_i9#(c4^8s51n'
DEBUG = True
ALLOWED_HOSTS = ['pwa-3609.rostiapp.cz','djangochat-4280.rostiapp.cz', '127.0.0.1', 'localhost']
# ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'corsheaders',
    'channels',
    'rest_auth',
    'rest_auth.registration',
    'rest_framework',
    'rest_framework.authtoken',

    'chat'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangochat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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

WSGI_APPLICATION = 'djangochat.wsgi.application'
ASGI_APPLICATION = 'djangochat.routing.application'
# ASGI_APPLICATION = 'djangochat.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
            # "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        # "ROUTING": "chat.routing.channel_routing",
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', }
]

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'cs-cz'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Prague'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# authentication settings

SITE_ID = 1
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
# CORS_ORIGIN_WHITELIST = ('localhost:3000')
# CORS_ORIGIN_WHITELIST = ('localhost:8000')
# CORS_ORIGIN_WHITELIST = ('*')
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'none'
CSRF_COOKIE_NAME = "csrftoken"

# HOST_URL = 'https://pwa-3609.rostiapp.cz'
HOST_URL = 'http://djangochat-4280.rostiapp.cz'
if DEBUG:
    HOST_URL = 'http://localhost:3000'
    # HOST_URL = 'http://localhost:8000'

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
    'localhost:8000',
    'localhost:8080',
    'djangochat-4280.rostiapp.cz',
    'djangochat-4280.rostiapp.cz:3000',
    'djangochat-4280.rostiapp.cz:8000',
    'djangochat-4280.rostiapp.cz:8080',
    'djangochat-4280.rostiapp.cz:8001',
    '127.0.0.1:3000',
    '127.0.0.1:8000',
    '127.0.0.1:8080',
    )