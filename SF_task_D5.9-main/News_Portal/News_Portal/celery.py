import os

from .settings import INSTALLED_APPS
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')


app.config_from_object('django.conf:settings') 


app.autodiscover_tasks(INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'send_mailing_monday_8am': {
        'task': 'news_paper.tasks.do_mailing',
        'schedule': crontab(day_of_week=1, hour=8, minute=0),
    },
}