from fastapi import FastAPI, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
import jwt

authenticator = OAuth2PasswordBearer(tokenUrl="login")

secret_key = "abcdefghij"
app = FastAPI()
expire_time = 10

def create_access_token(data: dict):
    global expire_time
    payload_to_encode = data.copy()
    expire_time = datetime.now() + timedelta(seconds=expire_time)
    payload_to_encode.update({"exp": expire_time})
    return jwt.encode(payload_to_encode, secret_key, algorithm="HS256")

def decode_jwt(token = Depends(authenticator)):
    try:
        data = jwt.decode(token, secret_key, "HS256")
        return data
    except:
        return {"status": "failed", "message": "Auth failed"}

@app.post("/login")
def demo( data: OAuth2PasswordRequestForm = Depends() ):

    token = create_access_token({"username": "rohit"})

    return {
        "access_token": token,
        "token_type": "bearer",
        "status": "completed."
    }


# @app.get("/demo")
# def demo(username: str, password: str):
#     if username == "vipin" and password == "123":

#         return {
#             "name": "vipin",
#             "age": "30",
#             "status": "completed."
#         }
#     else:
#         status_code = status.HTTP_401_UNAUTHORIZED
#         return {
#                     "status": "completed.",
#                     "message": "invalid username or password."
#                 }


@app.get("/user_info")
def test(token: str = Depends(decode_jwt)):
    return token


@app.get("/students")
def test(token: str = Depends(decode_jwt)):
    if token.get("username"):
        return {"name": "rohit", "age": 20}
    else:
        return token
