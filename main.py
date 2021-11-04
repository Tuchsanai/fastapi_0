from typing import Optional
from fastapi import FastAPI,Query, Body, Path
from router import blog_get, blog_post
from router import user,product


app = FastAPI()
app.include_router(blog_get.routerget)
app.include_router(blog_post.router_post)


@app.get("/")
def read_root():
    return {"Hello": "This is demo"}

