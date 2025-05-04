from fastapi import APIRouter, Depends
from src import get_db_session
from src.models import User
from pydantic import BaseModel

class UserRegister( BaseModel ):
    username : str
    password: str
    age: int
    role: str

user_router = APIRouter()


@user_router.post("/register_user")
def register_user( user: UserRegister , database = Depends( get_db_session )):

    user = User( name = UserRegister.username, password = UserRegister.password,
                role = UserRegister.role, age = UserRegister.age )
    database.add(user)
    database.commit()
    return { "msg": "User created done" }
