from celery import Celery
from config.constants import (
    CELERY_BROKER_URL, CELERY_RESULT_BACKEND, CELERY_TASK_SERIALIZER,
    CELERY_ACCEPT_CONTENT, CELERY_RESULT_SERIALIZER, CELERY_TIMEZONE, CELERY_ENABLE_UTC
)

celery_app = Celery('tasks', broker=CELERY_BROKER_URL)

celery_app.conf.update(
    result_backend=CELERY_RESULT_BACKEND,
    task_serializer=CELERY_TASK_SERIALIZER,
    accept_content=CELERY_ACCEPT_CONTENT,
    result_serializer=CELERY_RESULT_SERIALIZER,
    timezone=CELERY_TIMEZONE,
    enable_utc=CELERY_ENABLE_UTC,
)