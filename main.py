

from typing import Optional
from fastapi import FastAPI,Query, Body, Path
from router import blog_get, blog_post
from router import product


app = FastAPI()
app.include_router(blog_get.routerget)
app.include_router(blog_post.router_post)
app.include_router(product.router)


@app.get("/")
def read_root():
    return {"Hello": "This is demo"}
