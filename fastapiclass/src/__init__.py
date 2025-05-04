from fastapi import FastAPI

from sqlmodel import SQLModel, create_engine, Session
from src.models import User

app = FastAPI()

database_file = "sqlite:///database.db"

engine = create_engine( database_file )

SQLModel.metadata.create_all(engine)

def get_db_session():

    with Session(engine) as db:
        yield db

