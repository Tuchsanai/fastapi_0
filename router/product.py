from typing import Optional, List
from fastapi import APIRouter, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from fastapi.responses import JSONResponse

router = APIRouter(
  prefix='/product',
  tags=['product']
)

products = ['watch', 'camera', 'phone']



@router.get("/headers-and-object/")
def get_headers(response: Response):
    response.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}


@router.get("/headers/")
def get_headers():
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US"}
    return JSONResponse(content=content, headers=headers)


@router.post("/cookie-and-object/")
def create_cookie(response: Response):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}


@router.post("/cookie/")
def create_cookie():
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return response


@router.get('/all')
def get_all_products(response: Response):
  # return products
  data = " ".join(products)
  response = Response(content=data, media_type="text/plain")
  response.set_cookie(key="test_cookie", value="test_cookie_value")
  response.headers['custom_response_header'] = 'test header'
  return response


@router.post('/withheader')
def get_products( response: Response, custom_header: Optional[List[str]] = Header(None),  test_cookie: Optional[str] = Cookie(None)  ):
  if custom_header:
    response.headers['custom_response_header'] = " and ".join(custom_header)
  return {
    'data': products,
    'custom_header': custom_header,
    'my_cookie': test_cookie
  }





@router.get('/withheader')
def get_products(
  response: Response,
  custom_header: Optional[List[str]] = Header(None),
  test_cookie: Optional[str] = Cookie(None)
  ):
  if custom_header:
    response.headers['custom_response_header'] = " and ".join(custom_header)
  return {
    'data': products,
    'custom_header': custom_header,
    'my_cookie': test_cookie
  }


@router.get('/{id}', responses={
  200: {
    "content": {
      "text/html": {
        "example": "<div>Product</div>"
      }
    },
    "description": "Returns the HTML for an object"
  },
  404: {
    "content": {
      "text/plain": {
        "example": "Product not available"
      }
    },
    "description": "A cleartext error message"
  }
})
def get_product(id: int):
  if id > len(products):
    out = "Product not available"
    return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
  else:
    product = products[id]
    out = f"""
    <head>
      <style>
      .product {{
        width: 500px;
        height: 30px;
        border: 2px inset green;
        background-color: lightblue;
        text-align: center;
      }}
      </style>
    </head>
    <div class="product">{product}</div>
    """
    return HTMLResponse(content=out, media_type="text/html")