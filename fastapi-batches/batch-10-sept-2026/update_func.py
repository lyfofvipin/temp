from fastapi import FastAPI

data = [
    {
        "id": 1,
        "name": "Aarav Sharma",
        "email": "aarav.sharma@student.in",
        "phone": "+91 98765 43210",
        "city": "New Delhi",
        "state": "Delhi"
    },
    {
        "id": 2,
        "name": "Priya Patel",
        "email": "priya.patel@student.in",
        "phone": "+91 98234 56781",
        "city": "Ahmedabad",
        "state": "Gujarat"
    },
    {
        "id": 3,
        "name": "Rohan Mehta",
        "email": "rohan.mehta@student.in",
        "phone": "+91 97654 32109",
        "city": "Mumbai",
        "state": "Maharashtra"
    },
    {
        "id": 4,
        "name": "Ananya Iyer",
        "email": "ananya.iyer@student.in",
        "phone": "+91 98456 78901",
        "city": "Chennai",
        "state": "Tamil Nadu"
    },
    {
        "id": 5,
        "name": "Vikram Singh",
        "email": "vikram.singh@student.in",
        "phone": "+91 98123 45670",
        "city": "Jaipur",
        "state": "Rajasthan"
    },
    {
        "id": 6,
        "name": "Sneha Reddy",
        "email": "sneha.reddy@student.in",
        "phone": "+91 99087 65432",
        "city": "Hyderabad",
        "state": "Telangana"
    },
    {
        "id": 7,
        "name": "Arjun Nair",
        "email": "arjun.nair@student.in",
        "phone": "+91 97432 10987",
        "city": "Kochi",
        "state": "Kerala"
    },
    {
        "id": 8,
        "name": "Kavya Desai",
        "email": "kavya.desai@student.in",
        "phone": "+91 98321 09876",
        "city": "Pune",
        "state": "Maharashtra"
    },
    {
        "id": 9,
        "name": "Rahul Gupta",
        "email": "rahul.gupta@student.in",
        "phone": "+91 96543 21098",
        "city": "Lucknow",
        "state": "Uttar Pradesh"
    },
    {
        "id": 10,
        "name": "Ishita Banerjee",
        "email": "ishita.banerjee@student.in",
        "phone": "+91 93321 87654",
        "city": "Kolkata",
        "state": "West Bengal"
    }
]

app = FastAPI()

@app.get("/users")
def home():
    return data

@app.get("/user/{id}")
def home(id):

    if id.isdigit():
        id = int(id)
    else:
        return {
            "status": False,
            "message": "Invalid ID"
        }

    for x in data:
        if x["id"] == id:
            return x

    return {
        "status": False,
        "message": "User Not Found."
    }

@app.get("/student-stats")
def student_stats():
    return {
        "status": True,
        "Total": len(data),
        "name_start_with_a": len( [ x for x in data if x["name"].startswith("A") ] ),
        "message": "User Data Statistic Fetched."
    }

@app.post("/create_user")
def create_user(name, email, password, city="Jaipur", state="Raj"):

    data.append({
        "id": len(data) + 1,
        "name": name,
        "email": email,
        "password": password,
        "city": city,
        "state": state,
    })

    return {
        "status": True,
        "message": "User Created successfully."
    }


@app.delete("/delete_user")
def delete_user(id:int):


    for x in data:
        if x["id"] == id:
            data.remove(x)
            return {
                "status": True,
                "message": "User Deleted"
            }

    return {
        "status": False,
        "message": "Given ID Not Found In The Data."
    }


@app.put("/update")
def update_user(id: int, name="", email="", phone="", city="", state=""):

    for x in data:
        if x["id"] == id:

            if name: x["name"] = name
            
            if email: x["email"] = email

            if phone: x["phone"] = phone

            if city: x["city"] = city

            if state: x["state"] = state

            return {
                "status": True,
                "message": "User Info Has Updated."
            }

    return {
        "status": False,
        "message": "User Not Found."
    }

