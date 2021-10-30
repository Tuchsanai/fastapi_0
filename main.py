from typing import Optional
from fastapi import FastAPI
from router import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.routerget)
app.include_router(blog_post.router_post)


@app.get("/")
def read_root():
    return {"Hello": "This is demo"}

