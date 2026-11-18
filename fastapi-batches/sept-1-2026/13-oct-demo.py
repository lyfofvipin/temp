class UserModel:

    def __init__( self, id, name, email, password, role="customer", is_active=True):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.is_active = is_active

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

from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
def home():
    return "This is homepage."

@app.get("/health")
def health():
    return {"status": True}

@app.get("/users")
def all_data():
    return data


@app.post( "/create" )
def create(name=Form(), email=Form(), role=Form(), password=Form()):

    data.append(
        UserModel(
            id=len(data) + 1,
            name=name,
            email=email,
            password=password,
            role=role
        )
    )

    return {"status": True, "message": "User Created Done."}

@app.patch("/update_user")
def update_user( id: int, name:str = Form(default=""), email:str = Form(default=""), role=Form(default=""), password=Form(default="")  ):

    for x in data:
        if x.id == id:

            if name:
                x.name = name

            if email:
                x.email = email

            if role: x.role = role

            if password: x.password = password

            return {"status": True, "message": "User Updated"}

    return {"status": False, "message": "Invalid Id."}
