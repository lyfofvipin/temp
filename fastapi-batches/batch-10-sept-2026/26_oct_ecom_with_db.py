from sqlmodel import SQLModel, Field, create_engine, select, Session
from fastapi import FastAPI
from pydantic import BaseModel

class StudentModel(SQLModel, table=True):

    id: int = Field( primary_key=True )
    name:str = Field( min_length=3, max_length=16, nullable=False )
    email:str = Field( nullable=False, unique=True )
    phone:str = Field( nullable=False, unique=True )
    city:str = Field( nullable=False )
    state:str = Field( nullable=False )
    password:str = Field( nullable=False, default="Password@123" )

class StudentInput(BaseModel):
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


class ProductInput(BaseModel):
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


class OrderInput(BaseModel):
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

@app.get("/all_students")
def all_students():
    return {
           "status": True,
           "message": "Data Fetched Done.",
           "data": db.exec( select(StudentModel) ).all()
    }

@app.get("/all_students/{id}")
def all_students(id:int):
    data = db.exec( select(StudentModel).filter(StudentModel.id == id) ).one_or_none()
    return {
           "status": True if data else False,
           "message": "Data Fetched Done.",
           "data": data
    }


@app.get("/all_products")
def all_products():
    return {
           "status": True,
           "message": "Data Fetched Done.",
           "data": db.exec( select(ProductModel) ).all()
    }


@app.get("/all_products/{id:int}")
def all_products(id: int):
    data = db.exec( select(ProductModel).filter(ProductModel.id == id) ).one_or_none()
    return {
           "status": True if data else False,
           "message": "Data Fetched Done.",
           "data": data
    }


@app.post("/crete_student")
def create_student(student_data: StudentInput):
    student_data = StudentModel(
        name=student_data.name,
        email=student_data.email,
        phone=student_data.phone,
        city=student_data.city,
        state=student_data.state,
        password=student_data.password
    )
    db.add(student_data)
    db.commit()
    db.refresh(student_data)


@app.post("/crete_product")
def create_product(product_data: ProductInput):
    product_data = ProductModel(
        title=product_data.title,
        category=product_data.category,
        stock=product_data.stock,
        brand=product_data.brand,
        price=product_data.price
    )
    db.add(product_data)
    db.commit()
    db.refresh(product_data)

@app.post("/crete_order")
def create_order(order_data: OrderInput):

    validate_user = db.exec( select(StudentModel).filter(StudentModel.id == order_data.user_id) ).one_or_none()
    if not validate_user:
        return {"status": False, "message": "Invalid user id given."}

    validate_product = db.exec( select(ProductModel).filter(ProductModel.id == order_data.product_id) ).one_or_none()
    if not validate_product:
        return {"status": False, "message": "Invalid product id given."}

    if validate_product.stock < order_data.quantity:
        return {"status": False, "message": f"We are out of stock we only have {validate_product.stock} available."}
         

    order = OrderModel(
        user_id=order_data.user_id,
        product_id=order_data.product_id,
        quantity=order_data.quantity,
        payment_mode=order_data.payment_mode,
        status=order_data.status
    )

    validate_product.stock -= order_data.quantity

    db.add(order)
    db.add(validate_product)

    db.commit()
    db.refresh(order)
    db.refresh(validate_product)

