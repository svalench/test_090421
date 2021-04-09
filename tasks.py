import math

from celery_worker import celery


@celery.task(name="sqrt", bind=True)
def sqrt_find(value:int) -> float:
    return math.sqrt(value)