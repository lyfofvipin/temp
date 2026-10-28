from fastapi import FastAPI
from pydantic import BaseModel, Field

class UserModel(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=16)
    email: str = Field(pattern=".*@.*\..*$")
    password: str
    role: str = "customer"
    is_active: bool = True

    def __repr__(self):
        return f"{self.id} - {self.name} ({self.email})"

class UpdateUserModel(BaseModel):
    name: str = Field(min_length=3, max_length=16, default=None)
    email: str = Field(pattern=".*@.*\..*$", default=None)
    password: str = None
    role: str = None
    is_active: bool = None

    def __repr__(self):
        return f"{self.id} - {self.name} ({self.email})"


users = [
    (1, "Rahul Sharma", "rahul@example.com", "Rahul@123", "customer", True),
    (2, "Priya Verma", "priya@example.com", "Priya@123", "customer", True),
    (3, "Amit Singh", "amit@example.com", "Amit@123", "admin", True),
    (4, "Neha Gupta", "neha@example.com", "Neha@123", "customer", True),
    (5, "Vikram Patel", "vikram@example.com", "Vikram@123", "seller", True),
    (6, "Anjali Mehta", "anjali@example.com", "Anjali@123", "customer", True),
    (7, "Rohan Joshi", "rohan@example.com", "Rohan@123", "customer", False),
    (8, "Sneha Kapoor", "sneha@example.com", "Sneha@123", "seller", True),
    (9, "Arjun Malhotra", "arjun@example.com", "Arjun@123", "customer", True),
    (10, "Pooja Yadav", "pooja@example.com", "Pooja@123", "customer", True),
    (11, "Karan Shah", "karan@example.com", "Karan@123", "admin", True),
    (12, "Meera Nair", "meera@example.com", "Meera@123", "customer", True),
    (13, "Sahil Khan", "sahil@example.com", "Sahil@123", "seller", False),
    (14, "Isha Agarwal", "isha@example.com", "Isha@123", "customer", True),
    (15, "Dev Mishra", "dev@example.com", "Dev@123", "customer", True),
]

data = []

for u in users:
    data.append(
        UserModel(
            id=u[0],
            name=u[1],
            email=u[2],
            password=u[3],
            role=u[4],
            is_active=u[5]
        )
    )


app = FastAPI()

@app.get("/")
def all_users():
    return data

@app.post("/create_user")
def create( user_data:UserModel ):
    user_data.id = len(data) + 1
    data.append(user_data)
    return {"status": True, "message": "User created done."}

@app.post("/create_user/{id}")
def create( id: int, user_data:UpdateUserModel ):

    for x in data:
        if x.id == id:
            
            if user_data.name: x.name = user_data.name

            if user_data.email: x.email = user_data.email

            if user_data.password: x.password = user_data.password

            if user_data.role: x.role = user_data.role
            
            if user_data.is_active: x.is_active = user_data.is_active

    return {"status": False, "message": "Id Not Found."}

