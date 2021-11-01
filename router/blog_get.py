from fastapi import APIRouter, Response, status
from enum import Enum
from typing import Optional

routerget = APIRouter(prefix='/blog_get', tags=['blog'])


@routerget.get('/data')
def get1(page = 1, page_size: Optional[int] = None):
  return {'message': f'All {page_size} blogs on page {page}'}



@routerget.get('/all', summary='Retrieve all blogs',  description='This api call simulates fetching all blogs',
  response_description="The list of available blogs"
  )
def get_blogs(page = 1, page_size: Optional[int] = None):
  return {'message': f'All {page_size} blogs on page {page}'}
