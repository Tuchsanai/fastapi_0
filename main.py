from typing import Optional

from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get/")
def get(a : int, b : Optional[int]=15) :
    return { 'message': f' a = {a} b= {b}'  }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get('/blog/type/{type}', tags=['zzz'])
def get_blog_type(type: int):
  return {'message': f'Blog type {type}'}    