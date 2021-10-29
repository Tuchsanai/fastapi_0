from typing import Optional
from fastapi import FastAPI
from router import blog_get

app = FastAPI()
app.include_router(blog_get.routerget)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get/")
def get(a : int, b : Optional[int]=15) :
    return { 'message': f' a = {a} b= {b}'  }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
