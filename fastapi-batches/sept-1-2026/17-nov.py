from sqlmodel import SQLModel, Field, create_engine, Session, select

class Laptop(SQLModel, table=True):

    id: int = Field(primary_key=True)
    model: str = Field( min_length=3, max_digits=16 )
    num_of_keys:int
    usb_port: int
    power_supp: int

conn = create_engine("sqlite:///nov-17.db")

SQLModel.metadata.create_all(conn)

db = Session(conn)

query = select(Laptop).filter(Laptop.id == 1)

data = db.exec( query ).first()

db.delete(data)
db.commit()

