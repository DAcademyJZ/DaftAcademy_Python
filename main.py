from fastapi import FastAPI, Request, status
from pydantic import BaseModel
app = FastAPI()
app.counter = 0
class HelloResp(BaseModel):
    msg: str

@app.get("/")
def root(status_code=200):
    return {"message" : "Hello world!"}

@app.get("/hello/{name}")
def hello_name_view(name: str):
    return f"Hello {name}"



@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)

@app.get("/hello/{name}", response_model=HelloResp)
def hello_name_view(name: str):
    return HelloResp(msg=f"Hello {name}")



@app.get("/method/{item_id}",status_code=200)
def read_root(item_id: str, request: Request):
    if item_id == 'GET' or item_id == 'DELETE' or item_id == 'PUT' or item_id == 'OPTIONS':
        client_host = request.client.host
        return {"method": item_id}

