from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro_cli.settings')

app = Celery('pro_cli')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()