import os
from core.settings import env
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE', default='core.settings.production'))

application = get_wsgi_application()
