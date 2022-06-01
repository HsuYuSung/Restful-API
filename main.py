from fastapi import FastAPI, Response, status
from typing import Union
from pydantic import BaseModel
# from fastapi_log.log_request import LoggingRoute
from fastapi.encoders import jsonable_encoder
import uvicorn


app = FastAPI()

# app.router.route_class = LoggingRoute

items_db = {}

# class Item(BaseModel):
#     key = 'key1'
#     value = 'data1'

class Item(BaseModel):
    key: str
    value: str



class Item_value(BaseModel):
    value = "updated_data1"



@app.get("/")
async def root():
    return items_db

    
# # 1. POST /key
@app.post("/key", status_code=status.HTTP_201_CREATED)
async def post_key(item:Item, response:Response):
    if item.key in items_db:
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:
        items_db[item.key] = item.value
  

# # 2. GET /key
@app.get("/key", status_code=status.HTTP_200_OK)
async def get_key():
    key = []
    for item in items_db:
        key.append(item)
    return key


# # 3. GET /key/{key}
@app.get("/key/{key}", status_code=status.HTTP_404_NOT_FOUND)
async def get__key_item(key, response:Response):
    if key in items_db:
        response.status_code = status.HTTP_200_OK
        data = {key: items_db[key]}
        json_compatible_item_data = jsonable_encoder(data)
        return json_compatible_item_data


# 4. PUT /key/{key}
@app.put("/key/{key}", status_code=status.HTTP_200_OK)
async def put_key_item(key, item:Item_value, response:Response):
    if key in items_db:
        items_db[key] = item.value
    else:
        items_db[key] = item.value
        response.status_code = status.HTTP_201_CREATED

    data = items_db[key]
    json_compatible_item_data = jsonable_encoder(data)
    return json_compatible_item_data


# 5. DELETE /key/{key}
@app.delete("/key/{key:path}", status_code=status.HTTP_200_OK)
async def del_key(key: str):
    if key in items_db:
        items_db.pop(key)


if __name__ == "__main__":
    uvicorn.run(app, host="10.100.100.49", port=8000, log_level="info")
    #uvicorn.run(app, host="10.100.100.49", port=443, log_level="info")
    #uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
    #uvicorn.run(app, host="192.168.229.164", port=8000, log_level="info")
