from .base import *


DEBUG = False

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'plouc',
        'USER': 'lawiz',
        'PASSWORD':'Test123DH',
        'HOST':'mysql.lawiz.org',
        'OPTIONS'  : { 'init_command' : 'SET default_storage_engine=MyISAM', },
        'PORT':''

        
    }
}

STATIC_URL = '/'
STATIC_ROOT = os.path.join(BASE_DIR, '/home/lawiz22/plouc.live/public')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../public/media/')
