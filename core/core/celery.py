from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core') # name of the main module of application

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()