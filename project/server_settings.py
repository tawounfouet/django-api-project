from .settings import *

SECRET_KEY = '$!n(!5bk_4@(xcq4@hv&)3$fs&(3!@0x1j^(hma=4w7zbtz9$('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.spatialite',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# PostGIS database settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'django_pg_api_db',
#         'USER': 'postgres',
#         'PASSWORD': 'Divalt&2013',
#         'HOST': '52.143.134.24', # 127.0.0.1
#         'PORT': '5432',
#     }
# }

# pip install dj-database-url
import dj_database_url

from os import getenv
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


# DATABASES = {
#     'default': dj_database_url.config(
#         # default='postgres://...',
#         env="DATABASE_URL",
#         conn_max_age=600,
#         conn_health_checks=True,
#     )
# }


from os import getenv
from dotenv import load_dotenv

# Replace the DATABASES section of your settings.py with this
DATABASES = {
  'default': {
    #'ENGINE': 'django.db.backends.postgresql',
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': getenv('PGDATABASE'),
    'USER': getenv('PGUSER'),
    'PASSWORD': getenv('PGPASSWORD'),
    'HOST': getenv('PGHOST'),
    'PORT': getenv('PGPORT', 5432),
    'OPTIONS': {
      'sslmode': 'require',
    },
  }
}