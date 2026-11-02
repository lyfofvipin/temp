from sqlmodel import SQLModel, Field, create_engine, select, Session
from fastapi import FastAPI, Depends
from pydantic import BaseModel 
from fastapi.middleware.cors import CORSMiddleware


class StudentModel(SQLModel, table=True):

        id: int = Field( primary_key=True )
        name:str = Field( min_length=3, max_length=16, nullable=False )
        email:str = Field( nullable=False, unique=True )
        phone:str = Field( nullable=False, unique=True )
        city:str = Field( nullable=False )
        state:str = Field( nullable=False )
        password:str = Field( nullable=False, default="Password@123" ) # not a real password

class StudenInput(BaseModel):
        email:str = Field( nullable=False, unique=True )
        name:str = Field( min_length=3, max_length=16, nullable=False )
        phone:str = Field( nullable=False, unique=True )
        id: int = Field( primary_key=True )
        city:str = Field( nullable=False )
        state:str = Field( nullable=False )
        password:str = Field( nullable=False, default="Password@123" ) # not a real password

class ProductModel(SQLModel, table=True):

        id:int = Field( primary_key=True )
        title:str = Field( min_length=3, max_length=16, nullable=False )
        category: str = Field( min_length=3, max_length=16, nullable=False )
        price: float = Field( nullable=False, gt=0 )
        stock: int = Field( nullable=False, gt=0 )
        brand: str


class ProductInput(BaseModel):
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

class OrderInput(BaseModel):
        id:int = Field( primary_key=True )
        user_id: int = Field( nullable=False )
        product_id: int = Field( nullable=False )
        quantity: int = Field( nullable=False, gt=0 )
        payment_mode:str = Field( nullable=False )
        status: bool = Field( nullable=False, default=True )

database_path = "sqlite:///ecom_db.db"

connection = create_engine(database_path)

SQLModel.metadata.create_all(connection)

def db_conn_creator():
    with Session(connection) as db:
        yield db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://127.0.0.1:9000", "http://localhost:9000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.get("/dump_data")
# def dump_dummy_data():

#     users_data = [
#         StudentModel( name= "Aarav Sharma", email = "aarav.sharma@student.in", phone = "+91 98765 43210", city = "New Delhi", state = "Delhi"),
#     ]

#     products_data = [
#         ProductModel(title = "Wireless Bluetooth Headphones", category = "Electronics", price = 2999.00, stock=45, brand = "Boat"),
#     ]

#     orders_data = [
#         OrderModel(id=1001, user_id=1, product_id=101, quantity=1, payment_mode="UPI"),
#         OrderModel(id=1002, user_id=1, product_id=103, quantity=2, payment_mode="Credit Card"),
#         OrderModel(id=1003, user_id=2, product_id=102, quantity=1, payment_mode="Net Banking"),
#         OrderModel(id=1004, user_id=3, product_id=104, quantity=1, payment_mode="UPI"),
#         OrderModel(id=1005, user_id=3, product_id=105, quantity=1, payment_mode="COD"),
#         OrderModel(id=1006, user_id=5, product_id=101, quantity=2, payment_mode="Credit Card"),
#     ]

#     for x,y in zip(users_data, products_data):
#         db.add(x)
#         db.add(y)

#     for x in orders_data:
#         db.add(x)

#     db.commit()  

@app.get("/all_students")
def all_students(db = Depends(db_conn_creator)):
    # 1.return db.exec(select(StudentModel)).all()
    # 2.query = select(StudentModel)
    # result = db.exec(query)
    # return result.all()
    return{
           "status": "True",
           "Message":"Data fetched successfully",
           "data": db.exec(select(StudentModel)).all()
    }

@app.get("/all_students/{id}")
def all_students(id:int, db = Depends(db_conn_creator)):
    data= db.exec(select(StudentModel).filter(StudentModel.id)).one_or_none()
    return{
           "status": True if data else False,
           "Message":"Data fetched successfully",
           
    }

@app.get("/all_products")
def all_products(db = Depends(db_conn_creator)):
    return{
           "status": "True",
           "Message":"Data fetched successfully",
           "data": db.exec(select(ProductModel)).all()
    }

@app.get("/all_products/{id}")
def all_products(id:int, db = Depends(db_conn_creator)):
    data= db.exec(select(ProductModel).filter(ProductModel.id)).one_or_none()
    return{
           "status": True if data else False,
           "Message":"Data fetched successfully",
           
    }

@app.post("/create_student")
def create_student(student_data: StudenInput, db = Depends(db_conn_creator)):
    # new_student = StudentModel(**student_data.dict())
   
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

    return {
        "status": True,
        "message": "Student created successfully",
        "data": student_data
    }

@app.post("/create_product")
def create_product(product_data: ProductInput, db = Depends(db_conn_creator)):
   
    product_data = ProductModel(
        title=product_data.title,
        category=product_data.category,
        price=product_data.price,
        stock=product_data.stock,
        brand=product_data.brand
    )

    db.add(product_data)
    db.commit()
    db.refresh(product_data)

    return {
        "status": True,
        "message": "Product created successfully",
        "data": product_data
    }

@app.post("/create_order")
def create_order(order_data: OrderInput, db = Depends(db_conn_creator)):

    validate_user = db.exec(select(StudentModel).filter(StudentModel.id == order_data.user_id)).one_or_none() 
    if not validate_user:
        return {
            "status": False,
            "message": "User not found",
            "data": None
        }
    validate_product = db.exec(select(ProductModel).filter(ProductModel.id == order_data.product_id)).one_or_none()
    if not validate_product:
        return {
            "status": False,
            "message": "Product not found",
            "data": None
        }
    if validate_product.stock < order_data.quantity:
        return {
            "status": False,
            "message": f"Insufficient stock. We only have {validate_product.stock} items available.",
            "data": None
        }
   
    order_data= OrderModel(
        user_id=order_data.user_id,
        product_id=order_data.product_id,
        quantity=order_data.quantity,
        payment_mode=order_data.payment_mode,
        status=order_data.status   
    )

    validate_product.stock -= order_data.quantity

    db.add(order_data)
    db.commit()
    db.refresh(order_data)

    return {
        "status": True,
        "message": "Product created successfully",
        "data": order_data
    }

@app.put("/update_student/{id}")
def update_student(id:int, student_data: StudenInput, db = Depends(db_conn_creator)):
    existing_student = db.exec(select(StudentModel).filter(StudentModel.id == id)).one_or_none()
    if not existing_student:
        return {
            "status": False,
            "message": "Student not found",
            "data": None
        }
    
    existing_student.name = student_data.name
    existing_student.email = student_data.email
    existing_student.phone = student_data.phone
    existing_student.city = student_data.city
    existing_student.state = student_data.state
    existing_student.password = student_data.password

    db.add(existing_student)
    db.commit()
    db.refresh(existing_student)

    return {
        "status": True,
        "message": "Student updated successfully",
        "data": existing_student
    }

@app.put("/update_product/{id}")
def update_product(id:int, product_data: ProductInput, db = Depends(db_conn_creator)):
    existing_product = db.exec(select(ProductModel).filter(ProductModel.id == id)).one_or_none()
    if not existing_product:
        return {
            "status": False,
            "message": "Product not found",
            "data": None
        }
    
    existing_product.title = product_data.title
    existing_product.category = product_data.category
    existing_product.price = product_data.price
    existing_product.stock = product_data.stock
    existing_product.brand = product_data.brand

    db.add(existing_product)
    db.commit()
    db.refresh(existing_product)

    return {
        "status": True,
        "message": "Product updated successfully",
        "data": existing_product
    }

@app.put("/update_order/{id}")
def update_order(id:int, order_data: OrderInput, db = Depends(db_conn_creator)):
    existing_order = db.exec(select(OrderModel).filter(OrderModel.id == id)).one_or_none()
    if not existing_order:
        return {
            "status": False,
            "message": "Order not found",
            "data": None
        }
    
    existing_order.user_id = order_data.user_id
    existing_order.product_id = order_data.product_id
    existing_order.quantity = order_data.quantity
    existing_order.payment_mode = order_data.payment_mode
    existing_order.status = order_data.status

    db.add(existing_order)
    db.commit()
    db.refresh(existing_order)

    return {
        "status": True,
        "message": "Order updated successfully",
        "data": existing_order
    }

@app.delete("/delete_student/{id}")
def delete_student(id:int, db = Depends(db_conn_creator)):
    existing_student = db.exec(select(StudentModel).filter(StudentModel.id == id)).one_or_none()
    if not existing_student:
        return {
            "status": False,
            "message": "Student not found",
            "data": None
        }
    
    db.delete(existing_student)
    db.commit()

    return {
        "status": True,
        "message": "Student deleted successfully",
        "data": None
    }

@app.delete("/delete_product/{id}")
def delete_product(id:int, db = Depends(db_conn_creator)):
    existing_product = db.exec(select(ProductModel).filter(ProductModel.id == id)).one_or_none()
    if not existing_product:
        return {
            "status": False,
            "message": "Product not found",
            "data": None
        }
    
    db.delete(existing_product)
    db.commit()

    return {
        "status": True,
        "message": "Product deleted successfully",
        "data": None
    }

@app.delete("/delete_order/{id}")
def delete_order(id:int, db = Depends(db_conn_creator)):
    existing_order = db.exec(select(OrderModel).filter(OrderModel.id == id)).one_or_none()
    if not existing_order:
        return {
            "status": False,
            "message": "Order not found",
            "data": None
        }
    
    db.delete(existing_order)
    db.commit()

    return {
        "status": True,
        "message": "Order deleted successfully",
        "data": None
    }

@app.get("/all_orders")
def all_orders(db = Depends(db_conn_creator)):
    return{
           "status": "True",
           "Message":"Data fetched successfully",
           "data": db.exec(select(OrderModel)).all()
    }




