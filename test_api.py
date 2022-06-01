from fastapi import FastAPI, Response, status
from typing import Union

app = FastAPI()

keys = {}
items = []
# items_db = [{'item_name':"Foo"}, {"item_name":"Bar"}, {"item_name":"Baz"}]
items_db = []

@app.get("/")
async def root():
    return {"message": "Hello"}



# @app.post("/items")
# async def create_item(item):
#     items.append(item)
#     print(items)

#     return item



# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item




# @app.get("/items/")
# async def read_item(skip:int = 0, limit:int = 1):
#     return items_db[skip: skip + limit]


# # 1. POST /key
@app.post("/key", status_code=400)
async def post_key(key, value, response:Response):
    print(keys)
    if key not in keys:
        keys[key] = value
        response.status_code = status.HTTP_201_CREATED

# # 2. GET /key
@app.get("/key", status_code=200)
async def get_key():
    key = []
    for k, v in keys:
        key.append(k)
    return key

# # 3. GET /key/{key}
@app.get("/key/{key_id}")
async def get__key_item(key_id):
    if key_id in keys:
        return 
    else:
        return 

# # 4. PUT /key/{key} 
# @app.post("key/{key_id}")
# async def put_key_item(key_id, value):
#     if key in keys:
#         keys[key_id] = value
#         return JSONResponse(status_code=200)
#     else:
#         return JSONResponse(status_code=201)

# # 5. DELETE /key/{key}
# @app.post("key/{key_id}")
# async def del_key(key_id):
#     return JSONResponse(status_code=200)