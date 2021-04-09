from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'

app = Celery("tasks", backend=BROKER_URL, broker=BACKEND_URL)
