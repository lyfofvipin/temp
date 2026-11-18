from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select

class Food(SQLModel, table=True):

    id: int = Field( primary_key=True )
    price: int = Field( gt=1 )
    name: str
    cat: str

conn = create_engine("sqlite:///nov-18.db")

SQLModel.metadata.create_all(conn)

db = Session(conn)

app = FastAPI()

@app.post( "/add_item" )
def add_item( name: str, price:int, cat: str ):
    item = Food( name=name, price=price, cat=cat )
    db.add(item)
    db.commit()
    return {
        "status": True,
        "message": "Item Added Successfully."
    }

@app.get("/all_items")
def items():
    return {
        "status": True,
        "message": "Data Fetch Successfully.",
        "data": db.exec( select(Food) ).all()
    }

@app.get("/all_veg_items")
def items():
    return {
        "status": True,
        "message": "Data Fetch Successfully.",
        "data": db.exec( select(Food).filter(Food.cat == "veg") ).all()
    }

@app.get("/all_non_veg_items")
def items():
    return {
        "status": True,
        "message": "Data Fetch Successfully.",
        "data": db.exec( select(Food).filter(Food.cat == "non-veg") ).all()
    }

@app.get("/get_item_by_id/{id:int}")
def items(id:int):
    data = db.exec( select(Food).filter(Food.id == id) ).first()
    if data:
        return {
            "status": True,
            "message": "Data Fetch Successfully.",
            "data": data
        }
    else:
        return {
            "status": False,
            "message": "Data with above ID not found.",
            "data": []
        }

@app.patch("/update_price")
def update_price( id: int, new_price: int ):

    if new_price <= 0:
        return {
            "status": False,
            "message": "Invalid Value for Price it can not be 0 or less then 0.",
        }

    query = select(Food).filter(Food.id == id)
    data = db.exec(query).first()
    if data:

        data.price = new_price
        db.add(data)
        db.commit()
        return {
            "status": True,
            "message": "Price Item is updated.",
        }

    else:
        return {
            "status": False,
            "message": "Invalid ID of the item.",
        }

@app.patch("/update_name")
def update_name( id: int, new_name: str ):

    if len(new_name) < 3:
        return {
            "status": False,
            "message": "Invalid Value for name it can not be 0 or less then 0.",
        }

    query = select(Food).filter(Food.id == id)
    data = db.exec(query).first()
    if data:

        data.name = new_name
        db.add(data)
        db.commit()
        return {
            "status": True,
            "message": "Name Of The Item is updated.",
        }

    else:
        return {
            "status": False,
            "message": "Invalid ID of the item.",
        }

@app.patch("/update_cat")
def update_cat( id: int, new_cat: str ):

    query = select(Food).filter(Food.id == id)
    data = db.exec(query).first()
    if data:

        data.cat = new_cat
        db.add(data)
        db.commit()
        return {
            "status": True,
            "message": "Category of the Item is updated.",
        }

    else:
        return {
            "status": False,
            "message": "Invalid ID of the item.",
        }

@app.delete("/delete_item")
def delete_item(id:int):

    item = db.exec(select(Food).filter(Food.id == id)).first()
    if item:
        db.delete(item)
        db.commit()
        return {
            "status": True,
            "message": "Item is deleted.",
        }
    else:
        return {
                "status": False,
                "message": "Invalid ID of the item.",
            }

