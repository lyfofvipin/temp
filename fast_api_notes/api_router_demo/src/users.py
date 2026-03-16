from fastapi import HTTPException, Body, APIRouter, Depends
import bcrypt
from src.models import SessionDep, User
from src.auth import validate_login
from typing import Annotated

user_routes = APIRouter(tags=["user_management"])

@user_routes.get("/")
def home():
    return  {"message": "This is home page."}

@user_routes.post("/create_users")
def register(db : SessionDep, data = Body(...)):
    password = bcrypt.hashpw( data.get("password").encode("UTF-8"), salt=bcrypt.gensalt(14))
    data_for_entry = User(
        name=data.get("name"),
        username=data.get("username"),
        mob=data.get("mob"),
        age=data.get("age"),
        password=password
    )
    db.add(data_for_entry)
    db.commit()

    return  {"message": data}

@user_routes.get("/all_users")
def get_all_users(db : SessionDep, login_info: Annotated[str, Depends(validate_login)]):

    test = [ x.__dict__ for x in db.query(User).all()]
    for x in test:
        x.pop("_sa_instance_state")
        x.pop("password")

    return  {"message": test}

@user_routes.get("/get_by_username/{username}")
def register(username, db : SessionDep):

    test = db.query(User).filter(User.username == username).first()
    if not test:
        return HTTPException(409, "User not found.")
    return  {"message": test}

@user_routes.patch("/update_by_username/{username}")
def update(username, login_info: Annotated[str, Depends(validate_login)], db : SessionDep, data = Body(...)):

    data_in_db = db.query(User).filter( User.username == username ).first()
    if not data_in_db:
        return HTTPException(409, "User not found.")
    
    if username != login_info:
        return HTTPException(409, "You are not allowed to update any other user.")

    if data.get("password"):
        password = bcrypt.hashpw( data.get("password").encode("UTF-8"), salt=bcrypt.gensalt(14))
        data_in_db.password = password
    if data.get("name"):
        data_in_db.name = data.get("name")
    if data.get("mob"):
        data_in_db.mob = data.get("mob")
    if data.get("age"):
        data_in_db.age = data.get("age")
    
    db.add(data_in_db)
    db.commit()

    return  {"message": "User updated completed."}


@user_routes.delete("/delete_by_id/{username}")
def delete(username, login_info: Annotated[str, Depends(validate_login)], db : SessionDep):

    data_in_db = db.query(User).filter( User.username == username ).first()
    if not data_in_db:
        return HTTPException(409, "User id not found.")

    if username != login_info:
        return HTTPException(409, "You are not allowed to update any other user.")

    db.delete(data_in_db)
    db.commit()

    return  {"message": "User deleted completed."}










# {
# "username": "lyfofvipin",
# "name": "vipin",
# "mob": "8876699324",
# "age": 45,
# "password": "1234"
# }