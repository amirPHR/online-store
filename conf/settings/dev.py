from .common import * 

DEBUG = True
SECRET_KEY = 'django-insecure-mpi(%c8@or93zx-l*z#0h2n%hb6*v-p-k5o^hhsid@qvrh31r$'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online_shop',
        'USER': 'root',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}