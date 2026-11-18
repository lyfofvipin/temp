from sqlmodel import SQLModel, Field, create_engine

class User( SQLModel, table=True ):

    id : int = Field(primary_key=True)
    name: str
    email: str

connection = create_engine("sqlite///abc_db.db")

SQLModel.metadata.create_all(connection)
