from typing import Optional

from fastapi import FastAPI, HTTPException

from celery_worker import celery
from tasks import celery as celery_app
app = FastAPI()


@app.get("/{value}")
def square_pens(value: str):
    result = if_int(value)
    if (result['status']):
        celery_app.delay(int(value))
    else:
        raise HTTPException(status_code=400, detail=result['text'])
    return {"detail": "process start"}


def if_int(in_num: str) -> dict:
    """Функция проверяет является ли число уелым положительным
    in_num -- входная строка

    """
    try:
        if int(in_num) > 0:
            return {'status': True, 'text': "This is int"}
        else:
            return {'status': False, 'text': "This is int<0"}
    except ValueError:
        return {'status': False, 'text': "This is not int"}
