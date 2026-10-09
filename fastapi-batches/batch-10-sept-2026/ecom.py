from prod_user_data import users_data
from prod_user_data import orders_data
from prod_user_data import products_data
from prod_user_data import ProductModel, OrderModel, StudentModel

from fastapi import FastAPI, status, Response


app = FastAPI()

@app.get("/")
def home():
    return "This is homepage."

@app.get("/list_products")
def products():
    return products_data

@app.get("/get_product_by_id")
def get_by_id(id:int):

    for x in products_data:
        if x.id == id:
            return x

    return {"status": False, "message": "ID Not Found."}

@app.post("/create_prod")
def create_prod( title, category, price:float, stock:int, brand ):

    products_data.append( ProductModel(
        id= len(products_data) + 1,
        title=title,
        category=category,
        price=price,
        stock=stock,
        brand=brand
    ) )

    return {"status": True, "message": "Product Created."}

@app.patch("/update_prod")
def update_product( id:int, title="", category="", price:float|None=None, stock:int|None=None, brand=""):

    for x in products_data:
        if x.id == id:

            if title: x.title = title

            if category: x.category = category

            if price != None: x.price = price

            if stock != None: x.stock = stock

            if brand: x.brand = brand

            return {"status": True, "message": "Product Updated Done."}

    return {"status": False, "message": f"Product With {id} Not Found"}

@app.delete("/delete_prod")
def delete_prod(id:int):

    for x in products_data:
        if x.id == id:
            products_data.remove(x)

            return {"Status": True, "message": "Product Deleted Done."}

    return {"status": False, "message": f"Product With {id} Not Found"}

@app.get("/list_users")
def all_users():
    return users_data

@app.get("/get_user_by_id/{id}")
def get_by_id(id):
    id = int(id)

    for x in users_data:
        if x.id == id:
            return x

@app.post("/create_user")
def create_user(name, email, password, phone, city="Jaipur", state="Raj"):

    users_data.append(StudentModel(
        id=len(users_data) + 1,
        name=name,
        email=email,
        password=password,
        phone=phone,
        city=city,
        state=state
    ))

    return {
        "status": True,
        "message": "User Created successfully."
    }

@app.delete("/delete_user")
def delete_user(id:int):

    for x in users_data:
        if x.id == id:
            users_data.remove(x)
            return {
                "status": True,
                "message": "User Deleted"
            }

    return {
        "status": False,
        "message": "Given ID Not Found In The users_data."
    }

@app.put("/update_user")
def update_user(id: int, name="", email="", phone="", city="", state="", password=""):

    for x in users_data:
        if x.id == id:

            if name: x.name = name
            
            if email: x.email = email

            if phone: x.phone = phone

            if city: x.city = city

            if state: x.state = state
            
            if password: x.password = password

            return {
                "status": True,
                "message": "User Info Has Updated."
            }

    return {
        "status": False,
        "message": "User Not Found."
    }

@app.get("/list_orders")
def all_users():
    return orders_data

@app.post("/create_order")
def new_order( user_id:int, product_id:int, quantity:int ):

    if user_id not in [ x.id for x in users_data]:
        return {"status": False, "message": "User Not Found"}

    if product_id not in [ x.id for x in products_data]:
            return {"status": False, "message": "Product Not Found"}

    if quantity <= 0:
        return {"status": False, "message": "Invalid Value for quantity."}

    orders_data.append(
        OrderModel(
            id=1000 + len(orders_data) + 1,
            user_id=user_id,
            product_id=product_id,
            quantity=quantity
        )
    )
    return {"status": "Your Order Is Completed."}

