from .settings import *  # Import everything from settings.py
import os
import logging
# Enable debugging during tests to see detailed error outputs
DEBUG = True

# Test database configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_host = os.getenv('DB_HOST')

logger.debug(f"DB_NAME: {db_name}")
logger.debug(f"DB_USER: {db_user}")
logger.debug(f"DB_HOST: {db_host}")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'HOST': os.getenv('DB_HOST'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT' : '5432',
    }
}

# Use a different secret key for testing
SECRET_KEY = 'testing-secret-key'

# Restrict allowed hosts for testing
ALLOWED_HOSTS = ['hobbyhive-dbhtapemgpdeayc7.northcentralus-01.azurewebsites.net']

CORS_ALLOWED_ORIGINS = [
    "https://hobbyhive-dbhtapemgpdeayc7.northcentralus-01.azurewebsites.net",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# Adjust media settings for testing (use temporary storage)
MEDIA_ROOT = BASE_DIR / 'test_media'
os.makedirs(MEDIA_ROOT, exist_ok=True)

