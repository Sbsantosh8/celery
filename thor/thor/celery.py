from __future__ import absolute_import, unicode_literals
import os
from celery.schedules import crontab
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thor.settings')

app = Celery('thor')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Look for task modules in Django applications.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app = Celery('thor')
app.conf.timezone = 'Asia/Kolkata'
app.conf.enable_utc = False





# Add periodic tasks
app.conf.beat_schedule = {
   
    'send-email-every-monday-9am': {
        'task': 'app.tasks.send_scheduled_email',
        'schedule': crontab(hour=15, minute=44, day_of_week=2),  # Runs every Monday at 9 AM
         
    },
}
