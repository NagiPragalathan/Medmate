# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Medmate.settings')

app = Celery('Medmate')

# Using a string here means the worker doesn't have to serialize the configuration object
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
