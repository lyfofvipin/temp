from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.models import SessionDep, User
import bcrypt

login_logout = APIRouter(tags=["auth_management"])

@login_logout.post("/login")
def login_user( data: Annotated[OAuth2PasswordRequestForm, Depends()], db: SessionDep ):
    
    user_data = db.query(User).filter(User.username == data.username).first()
    if not user_data:
        return HTTPException(401, "Given Username Not Found In The DB.")

    passwd_check = bcrypt.checkpw( data.password.encode("UTF-8"), user_data.password )
    if not passwd_check:
        return HTTPException(401, f"Invalid Password For {data.username}.")

    return {
        "access_token": data.username,
        "message": "Login Successfully."
    }

validate_login = OAuth2PasswordBearer(tokenUrl="login")
