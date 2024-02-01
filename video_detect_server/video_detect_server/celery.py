import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTING_MODULE', 'video_detect_server.settings')

app = Celery('video_detect_server')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
