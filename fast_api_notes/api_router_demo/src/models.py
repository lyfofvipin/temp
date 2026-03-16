from sqlmodel import  SQLModel, Field, create_engine, Session, select
from typing import Annotated
from fastapi import Depends

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    username: str = Field(unique=True, nullable=False)
    mob: str = Field(unique=True, nullable=False)
    age: int
    password: str = Field(nullable=False)

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_username: str
    title: str
    description: str
    status: bool = False

sqlite_url = f"sqlite:///database.db"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
