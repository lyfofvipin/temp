from fastapi import FastAPI
from prod_data import data, ProductModel


app = FastAPI()


@app.get("/")
def home():
    return "This is homepage."


@app.get("/products")
def products():
    return data


@app.delete("/delete_prod")
def delete(id:int):

    for x in data:
        if x.id == id:
            data.remove(x)
            return {"status": True, "message": "Item Deleted."}

    return {"status": False, "message": "Data Not Found"}


@app.post("/products/add")
def create_item( title, category, price:float, stock:int, brand, is_active:bool ):

    data.append(
        ProductModel(
            id= len(data) + 1,
            title=title,
            category=category,
            price=price,
            stock=stock,
            brand=brand,
            is_active=is_active
        )
    )

    return {"status": True, "message": "Product Added."}



@app.put("/update_prod")
def create_item(id:int, title="", category="", price:float=0, stock:int|None=None, brand="", is_active:bool|None=None ):

    for x in data:

        if x.id == id:

            if title: x.title = title

            if category: x.category = category

            if price: x.price = price

            if stock == None:
                pass
            else:
                x.stock = stock

            if brand: x.brand = brand

            if is_active != None: x.is_active = is_active

            return {"status": True, "message": "Prod updated"}

    return {"status": False, "message": "Prod not found."}
