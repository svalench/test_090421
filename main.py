from typing import Optional

from fastapi import FastAPI, HTTPException, Query

from celery_worker import app as celery
from tasks import sqrt_find
app = FastAPI()


@app.get("/")
def square_pens(value: str=Query(''),degree:int=Query(2)):
    print(type(value))
    result = if_int(value)
    if (result['status']):
        task = sqrt_find.delay(int(value),degree)
        print(task)
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
