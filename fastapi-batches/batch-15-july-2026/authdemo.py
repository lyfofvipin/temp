from fastapi import FastAPI, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import jwt

authenticator = OAuth2PasswordBearer(tokenUrl="login")

key = "abcdefghij"
app = FastAPI()

def decode_jwt(token):
    try:
        data = jwt.decode(token, key, "HS256")
        return data
    except:
        return {"status": "failed", "message": "Auth failed"}

@app.post("/login")
def demo( data: OAuth2PasswordRequestForm = Depends() ):

    data_to_encode = {"username": data.username}

    token = jwt.encode(data_to_encode, key, "HS256")

    return {
        "access_token": token,
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
