from typing import Annotated

from fastapi import Depends, FastAPI, Response, status, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login(data: Annotated[OAuth2PasswordRequestForm, Depends()], resp:Response):
    if data.username == "admin" and data.password == "123":
        return {"access_token": data.username, "token_type": "bearer"}
    else:
        resp.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "login fail"}

@app.get("/items/")
def read_items(data_from_login_api: Annotated[str, Depends(oauth2_scheme)]):
    return {"data_from_login_api": data_from_login_api}

@app.get("/home")
def read_items(data_from_login_api: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "Home Page"}

@app.get("/")
def home():
    return HTMLResponse("""
    <h1>Hi</h1>
    <h2>Hi</h2>
    """)
















# class Dummy(BaseModel):
#     username: str
#     password: str
#     client_id: str


# @app.post("/test")
# def login(data: Annotated[Dummy, Form()], resp:Response):
#     if data.username == "admin" and data.password == "123":
#         return {"message": "login done"}
#     else:
#         resp.status_code = status.HTTP_401_UNAUTHORIZED
#         return {"message": "login fail"}

