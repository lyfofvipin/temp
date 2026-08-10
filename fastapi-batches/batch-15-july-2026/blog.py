from fastapi import FastAPI, status, Response, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from sqlmodel import SQLModel, create_engine, Session, Field, Relationship
from pydantic import BaseModel
from datetime import datetime, timedelta

app = FastAPI()

sercret_key = "hello_this_is_a_test_key"
jwt_exp_time = 30
authorizer = OAuth2PasswordBearer("login")

class Posts(SQLModel, table=True):
    id : int = Field(primary_key=True, nullable=False)
    title: str = Field(nullable=False, unique=True)
    user_id: int = Field(nullable=False)
    desc: str

class Users(SQLModel, table=True):
    id : int = Field(primary_key=True, nullable=False)
    username: str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)
    mail: str = Field(nullable=False, unique=True)
    role: str = Field(nullable=False, default="non-admin")
    mob: str = Field(nullable=False, unique=True)

class PostForm(BaseModel):
    title: str
    desc: str | None = ""

class UserForm(BaseModel):
    username: str
    mail: str
    role: str = "non-admin"
    password: str
    mob: str

class UserUpdateForm(BaseModel):
    username: str | None = None
    mail: str | None = None
    role: str = "non-admin"
    password: str  | None = None
    mob: str | None = None

class PostUpdateForm(BaseModel):
    title: str | None = None
    desc: str | None = None


db_file = create_engine( "sqlite:///database.db" )

SQLModel.metadata.create_all(db_file)

def db_inj():
    with Session(db_file) as db:
        yield db

def encode(data: dict) -> str:
    data["exp"] = datetime.now(tz=None) + timedelta(minutes=jwt_exp_time)
    return jwt.encode(data, sercret_key, "HS256")

def decode(token: str = Depends(authorizer)):
    try:
        data = jwt.decode(token, sercret_key, "HS256")
        data.pop("exp")
        return data
    except:
        return False

@app.post("/login")
def login(response: Response, data = Depends(OAuth2PasswordRequestForm), db = Depends(db_inj)):
    user = db.query(Users).filter( Users.username == data.username, Users.password == data.password ).first()

    if user:
        token_data = {
            "username": user.username,
            "id": user.id,
            "role": user.role
        }
        return {
            "status": True,
            "message": "Token Created Successful",
            "access_token": encode(token_data)
        }
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {
            "status": False,
            "message": "Invalid User Info"
        }

@app.post("/create_user")
def create_user(response : Response, data : UserForm, db = Depends(db_inj)):

    data_to_add = Users(
        username=data.username,
        mob=data.mob,
        mail=data.mail,
        role=data.role,
        password=data.password
    )

    db.add(data_to_add)
    db.commit()

    response.status_code = status.HTTP_201_CREATED
    return {
        "status": True,
        "message": f"User {data.username} Created."
    }

@app.put("/update_user")
def update_user(response: Response, id: int, data: UserUpdateForm, db = Depends(db_inj), user_data = Depends(decode)):

    user = db.query(Users).filter(Users.id == id).first()
    if not user.username == user_data.get("username"):
        response.status_code = status.HTTP_403_FORBIDDEN
        return {
            "status": False,
            "message": "You are not allowed to update this user."
        }
    if user:
        if data.username: user.username = data.username
        if data.mail: user.mail = data.mail
        if data.mob: user.mob = data.mob
        if data.password: user.password = data.password
        if data.role: user.role = data.role

        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "status": True,
            "message": "User Updated Successfully."
        }
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status": False,
            "message": f"User with id {id} not found."
        }

@app.delete("/delete_user")
def delete_user(response: Response, id: int, db = Depends(db_inj), user_data = Depends(decode)):

    user = db.query(Users).filter(Users.id == id).first()
    if user:
        db.delete(user)
        db.commit()

        return {
            "status": True,
            "message": "User Deleted Successfully."
        }
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status": False,
            "message": f"User with id {id} not found."
        }

@app.get("/read_user")
def read_user(response: Response, db = Depends(db_inj), user_data = Depends(decode)):

    users = db.query(Users).filter(Users.id == user_data.get("id")).all()
    return {
        "status": True,
        "data": users,
        "message": "User Fetched Successfully."
    }

@app.post("/create_blog")
def create_blog(response: Response, data: PostForm, db = Depends(db_inj), user_data = Depends(decode)):

    data_to_add_in_db = Posts(
        title=data.title,
        desc=data.desc,
        user_id=user_data.get("id")
    )
    db.add(data_to_add_in_db)
    db.commit()

    response.status_code = status.HTTP_201_CREATED
    return {
        "status": True,
        "message": "Blog Created Successful."
    }

@app.post("/update_blog/{id}")
def update(response: Response, id:int, data: PostUpdateForm, db = Depends(db_inj), user_data = Depends(decode)):

    post = db.query(Posts).filter(Posts.id == id).first()
    if post:
        if data.title: post.title = data.title
        if data.desc: post.desc = data.desc

        db.add(post)
        db.commit()
        db.refresh(post)

        return {
            "status": True,
            "message": "Post Updated Successfully."
        }
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status": False,
            "message": f"Post with id {id} not found."
        }

@app.delete("/delete_post")
def delete_post(response: Response, id: int, db = Depends(db_inj), user_data = Depends(decode)):

    post = db.query(Posts).filter(Posts.id == id).first()
    if post:
        db.delete(post)
        db.commit()
        return {
            "status": True,
            "message": "Post Deleted Successfully."
        }
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status": False,
            "message": f"Post with id {id} not found."
        }

@app.get("/read_post")
def read_post(db = Depends(db_inj)):

    posts = db.query(Posts).all()
    return {
        "status": True,
        "data": posts,
        "message": "post Fetched Successfully."
    }

@app.get("/admin/read_user")
def read_user(response: Response, db = Depends(db_inj), user_data = Depends(decode)):

    if user_data.get("role") == "admin":
        users = db.query(Users).all()
        return {
            "status": True,
            "data": users,
            "message": "User Fetched Successfully."
        }
    else:
        response.status_code = status.HTTP_403_FORBIDDEN
        return {
            "status": False,
            "message": "You are not allowed to access this page."
        }