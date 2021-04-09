import math

from celery_worker import app


@app.task
def sqrt_find(value:int) -> float:
    return math.sqrt(value)