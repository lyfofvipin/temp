from sqlmodel import SQLModel, create_engine, Session, Field, select
from fastapi import FastAPI

class User( SQLModel, table=True ):

    id: int = Field( primary_key=True, nullable=False )
    name : str = Field( nullable=False )
    email : str = Field( nullable=False, unique=True )
    phone : str = Field( nullable=False, unique=True )
    city : str
    state : str

db_file_name = "sqlite:///user_data.db"

connection = create_engine(db_file_name)

SQLModel.metadata.create_all(connection)

tr = Session(connection)

app = FastAPI()

@app.get("/")
def home():
    return tr.exec( select(User) ).all()

@app.get("/get_by/{id}")
def get_by_id(id:int):
    data = tr.exec( select(User).filter(User.id == id) ).first()
    if data:
        return {"status": True, "data": data, "message": "Data Fetch Done."}
    else:
        return {"status": False, "message":"Invalid ID"}

@app.post("/crete_user")
def create_user(data: User):
    tr.add(data)
    tr.commit()
    return {"status": True, "Message": "User Created Done."}


@app.delete("/delete_user/{id:int}")
def delete_data(id:int):

    query = select(User).where(User.id == id)
    data = tr.exec( query ).one_or_none()
    if data:
        tr.delete(data)
        tr.commit()
    else:
        return {"status": False, "message": "Data Not Found."}
