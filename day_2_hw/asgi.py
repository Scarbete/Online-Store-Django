import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day_2_hw.settings')

application = get_asgi_application()
