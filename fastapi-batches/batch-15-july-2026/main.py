from fastapi import FastAPI, Form, status, Depends
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, create_engine, Session, select

class User1(BaseModel):
    name: str
    mail:str
    age:int

class User(SQLModel, table=True):
    id : int = Field( primary_key = True, nullable=False)
    name: str
    mail:str = Field( nullable=False, unique=True )
    age:int = Field(ge=18)

class Post(SQLModel, table=True):
    id : int = Field( primary_key = True, nullable=False)
    title: str = Field( nullable=False, unique=True )
    desc : str

class UserPostForm(BaseModel):
    title: str
    desc:str


app = FastAPI()

db_file = "sqlite:///dbfile.db"

db = create_engine(db_file)

SQLModel.metadata.create_all(db)

def db_dep_injection():
    with Session(db) as db_connection:
        yield db_connection

@app.get("/test")
def test( a : int = 1, b: str =2 ):
    return {
        "a": a,
        "b": b
    }

@app.post("/test_dict")
def test( data: dict ):
    return data

@app.post("/test_json")
def test_json(data: User1):
    return data

@app.post("/test_post")
def test( a : int = Form(...), b: str = Form(...) ):
    return {
        "a": a,
        "b": b
    }

@app.post("/test_db_class")
def test_json(data: User, db = Depends(db_dep_injection)):

    db.add(data)
    db.commit()
    return {"message" : "User Created", "status": "Done"}

@app.get("/get_user/{id}")
def test_json(id: int, db = Depends(db_dep_injection)):

    data = db.query(User).get(id)
    if data:
        return { 
                "name": data.name,
                "mail": data.mail,
                "age": data.age,
                "message": "Data Fetch Done",
                "status": "done"
            }
    else:
        status_code = status.HTTP_204_NO_CONTENT
        return {
                "message": "No User Found",
                "status": "done"
            }


@app.get("/age_above_20")
def test_json(db = Depends(db_dep_injection)):

    data = db.query(User).filter( User.age >= 20 ).all()
    return data

@app.patch("/createpost")
def post_create( data: UserPostForm, db = Depends(db_dep_injection) ):
    db_data = Post(
        title = data.title,
        desc = data.desc
    )
    db.add(db_data)
    db.commit()
    return {"status": True, "data": data, "message": "User Created Done"}

