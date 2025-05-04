from fastapi import APIRouter

from pydantic import BaseModel

home_router = APIRouter()


@home_router.get("/")
def home():
    """
        This is my home API.
    """
    return { "msg": "Home" }

@home_router.get("/about")
def about():
    """
        This is my about API.
    """
    return { "msg": "About" }

@home_router.get("/greet/{name:str}")
def greet(name):

    return { "msg": f"Hello {name}." }


@home_router.post("/user_data")
def take_user_data( username: str, password: str ):

    return [ username, password ]



class user_info( BaseModel ):
    username: str = "Enter Username"
    password: int | str = "Enter Password"
    age: int = 18
    bank: None | int = None


@home_router.post("/user_info")
def take_user_info( data: user_info ):

    return [ data.username, data.password, data.age, data.bank ]
