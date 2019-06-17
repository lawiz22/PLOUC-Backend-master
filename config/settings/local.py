from .base import *


DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'plouc',
        'USER': 'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':''

        
    }
}

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware', )

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
