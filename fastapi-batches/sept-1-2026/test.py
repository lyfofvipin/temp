from sqlmodel import SQLModel, Field, create_engine, Session, select

class User(SQLModel, table=True):

    id : int = Field( primary_key=True )
    username : str = Field( nullable=False, unique=True )
    password: str
    mob: str
    mail: str
    age: str = Field( nullable=False, gt=0 )
    dob: str

class Car(SQLModel, table=True):
    id : int = Field( primary_key=True )
    name: str
    model: str
    price : float
    discount: float

connection = create_engine("sqlite:///16-nov.db")

SQLModel.metadata.create_all(connection)

tr_var = Session(connection)

query = select(User).filter(User.mail == "v2ipin@gmail.com")

print( tr_var.exec( query ).first() )

# p = Car(name="Honda Civic", model=2024, price=2300000, discount=10)

# tr_var.add(p)

# tr_var.commit()
