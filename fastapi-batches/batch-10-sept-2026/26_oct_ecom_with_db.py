from sqlmodel import SQLModel, Field, create_engine, select, Session
from fastapi import FastAPI

class StudentModel(SQLModel, table=True):

        id: int = Field( primary_key=True )
        name:str = Field( min_length=3, max_length=16, nullable=False )
        email:str = Field( nullable=False, unique=True )
        phone:str = Field( nullable=False, unique=True )
        city:str = Field( nullable=False )
        state:str = Field( nullable=False )
        password:str = Field( nullable=False, default="Password@123" )

class ProductModel(SQLModel, table=True):

        id:int = Field( primary_key=True )
        title:str = Field( min_length=3, max_length=16, nullable=False )
        category: str = Field( min_length=3, max_length=16, nullable=False )
        price: float = Field( nullable=False, gt=0 )
        stock: int = Field( nullable=False, gt=0 )
        brand: str

class OrderModel(SQLModel, table=True):

        id:int = Field( primary_key=True )
        user_id: int = Field( nullable=False )
        product_id: int = Field( nullable=False )
        quantity: int = Field( nullable=False, gt=0 )
        payment_mode:str = Field( nullable=False )
        status: bool = Field( nullable=False, default=True )

database_path = "sqlite:///ecom_db.db"

connection = create_engine(database_path)

SQLModel.metadata.create_all(connection)

db = Session(connection)

app = FastAPI()

@app.get("/dump_data")
def dump_dummy_data():

    users_data = [
        StudentModel( name= "Aarav Sharma", email = "aarav.sharma@student.in", phone = "+91 98765 43210", city = "New Delhi", state = "Delhi"),
    ]

    products_data = [
        ProductModel(title = "Wireless Bluetooth Headphones", category = "Electronics", price = 2999.00, stock=45, brand = "Boat"),
    ]

    orders_data = [
        OrderModel(id=1001, user_id=1, product_id=101, quantity=1, payment_mode="UPI"),
        OrderModel(id=1002, user_id=1, product_id=103, quantity=2, payment_mode="Credit Card"),
        OrderModel(id=1003, user_id=2, product_id=102, quantity=1, payment_mode="Net Banking"),
        OrderModel(id=1004, user_id=3, product_id=104, quantity=1, payment_mode="UPI"),
        OrderModel(id=1005, user_id=3, product_id=105, quantity=1, payment_mode="COD"),
        OrderModel(id=1006, user_id=5, product_id=101, quantity=2, payment_mode="UPI"),
    ]

    for x,y in zip(users_data, products_data):
        db.add(x)
        db.add(y)

    for x in orders_data:
        db.add(x)

    db.commit()

