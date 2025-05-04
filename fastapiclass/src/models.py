from sqlmodel import SQLModel, Field


class User( SQLModel, table = True ):
    id: int = Field( primary_key = True, nullable = False )
    name: str = Field( nullable= False )
    password: str = Field( nullable= False )
    role: str = Field( nullable= False, default="user" )
    age: int

