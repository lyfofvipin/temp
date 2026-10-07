from database import data, StudentModel

from fastapi import FastAPI, status, Response


app = FastAPI()

@app.get("/")
def home():
    return "This is the homepage."

@app.get("/users")
def all_users():
    return data

@app.get("/user/{id}")
def get_by_id(id):
    id = int(id)

    for x in data:
        if x.id == id:
            return x

@app.post("/create_user")
def create_user(name, email, password, phone, response: Response, city="Jaipur", state="Raj"):

    data.append(StudentModel(
        id=len(data) + 1,
        name=name,
        email=email,
        password=password,
        phone=phone,
        city=city,
        state=state
    ))

    response.status_code = status.HTTP_201_CREATED
    return {
        "status": True,
        "message": "User Created successfully."
    }

@app.delete("/delete_user")
def delete_user(id:int, response: Response):

    for x in data:
        if x.id == id:
            data.remove(x)
            return {
                "status": True,
                "message": "User Deleted"
            }

    response.status_code = status.HTTP_404_NOT_FOUND
    return {
        "status": False,
        "message": "Given ID Not Found In The Data."
    }

@app.put("/update")
def update_user(id: int,response:Response, name="", email="", phone="", city="", state="", password=""):

    for x in data:
        if x.id == id:

            if name: x.name = name
            
            if email: x.email = email

            if phone: x.phone = phone

            if city: x.city = city

            if state: x.state = state
            
            if password: x.password = password

            response.status_code = status.HTTP_202_ACCEPTED
            return {
                "status": True,
                "message": "User Info Has Updated."
            }

    response.status_code = status.HTTP_404_NOT_FOUND
    return {
        "status": False,
        "message": "User Not Found."
    }

