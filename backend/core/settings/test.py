from .base import *

# Enable debug mode for testing
DEBUG = True

# Allow all hosts for testing
ALLOWED_HOSTS = ['*']

# Use SQLite database for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_test.sqlite3',
    }
}

# Test-specific settings
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
