from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()

class CarCreate( BaseModel ):

    id: int = Field(gt=0)
    brand: str = Field(min_length=3, max_length=10)
    model: str
    email: str = Field(pattern="^\S+@\S+\.\S+$")
    year: int
    price: float = Field(gt=5)

class CarUpdate( BaseModel ):

    brand: str | None = Field(min_length=3, max_length=10, default=None)
    model: str | None = None
    email: str | None = Field(pattern="^\S+@\S+\.\S+$", default=None)
    year: int | None = None
    price: float | None = Field(gt=50000, default=None)
    is_available: bool | None = None

data = [
    CarCreate(
        id=1,
        model="model1",
        brand="brand1",
        email="abc@gmail.com",
        year=2025,
        price=5000,
    ),
    CarCreate(
        id=2,
        model="model2",
        brand="brand2",
        email="abc@gmail.com",
        year=2025,
        price=5000,
    ),
    CarCreate(
        id=3,
        model="model3",
        brand="brand3",
        email="abc@gmail.com",
        year=2025,
        price=5000,
    )
]

@app.get("/")
def list_cars():
    return data

@app.post("/create")
def create_cars(car_data: CarCreate):
    data.append(car_data)
    return {"status": True, "message": "Car Data Added Successfully."}

@app.patch("/update")
def update( id: int, car_data:CarUpdate ):

    for x in data:
        if x.id == id:

            if car_data.brand: 
                x.brand = car_data.brand

            if car_data.email:
                x.email = car_data.email

            if car_data.model :
                x.model = car_data.model

            return {"status": True, "message":"Car updated successfully."}

    return  {"status": False, "message": "No car found with above ID."}

