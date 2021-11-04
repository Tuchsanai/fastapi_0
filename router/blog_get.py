from fastapi import APIRouter, Response, status
from fastapi import Query, Body, Path
from enum import Enum
from typing import Optional,List, Dict
from pydantic import BaseModel

import numpy as np

routerget = APIRouter(prefix='/blog_get', tags=['blog_get'])

class BlogModel(BaseModel):
    url: str = 'gg'
    alias: str ='zz'
    vblog : List[float] =[1.0,3.0]

@routerget.get('/test_data')
def test_data(blog : BlogModel ,id = 1, page_size: Optional[int] = None, v: Optional[List[float]] = Query( np.random.randn(3).tolist() )  ):
    print(type(np.array(v)))
    print(np.array(v).shape)
    return {'blog':blog,'message': f'id = {id} page = {page_size} , v={v}'}



@routerget.get('/all', summary='Retrieve all blogs',  description='This api call simulates fetching all blogs',
  response_description="The list of available blogs" )
def get_blogs(page = 1, page_size: Optional[int] = None):
  return {'message': f'All {page_size} blogs on page {page}'}
