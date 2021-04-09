import math

from celery_worker import app


@app.task
def sqrt_find(value: int, degree=2) -> float:
    if degree == 2:
        return math.sqrt(value)
    else:
        return pow(value, 1 / degree)
