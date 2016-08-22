# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8q^q#^j*4i1tg$!3iqvb_mohx#wcl1_ufvqhhd*%_80ow5zf29'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shopping',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}
