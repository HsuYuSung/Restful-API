from fastapi import FastAPI, Response, status
from typing import Union
from fastapi_log.log_request import LoggingRoute


app = FastAPI()

app.router.route_class = LoggingRoute

items_db = []


@app.get("/")
async def root():
    return {"message": "Hello"}


# # 1. POST /key
@app.post("/key", status_code=201)
async def post_key(key, value, response:Response):
    key_exist = False
    for item in items_db:
        if key in item:
            response.status_code = status.HTTP_400_BAD_REQUEST
            key_exist = True
            break
    
    if not key_exist:
        items_db.append({key:value})
    print(items_db)
    return
    
    

# # 2. GET /key
@app.get("/key", status_code=200)
async def get_key():
    key = []
    for item in items_db:
        for k in item:
            key.append(k)
    return key



# # 3. GET /key/{key}
@app.get("/key/{key_id}", status_code=404)
async def get__key_item(key_id, response:Response):
    for item in items_db:
        if key_id in item:
            response.status_code = status.HTTP_200_OK
            return item


# 4. PUT /key/{key}
@app.put("key/{key_id}", status_code=201)
async def put_key_item(key_id, value, response:Response):
    key_exist = False
    for item in items_db:
        if key_id in item:
            item[key_id] = value
            response.status_code = status.HTTP_200_OK
            key_exist = True
    
    if not key_exist:
        items_db.append({key_id: value})


# 5. DELETE /key/{key}
@app.delete("key/{key_id}", status_code=200)
async def del_key(key_id):
    for item in items_db:
        if key_id in item:
            items_db.remove(item)

