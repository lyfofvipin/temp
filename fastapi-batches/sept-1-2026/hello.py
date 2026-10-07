from fastapi import FastAPI

abc = FastAPI()

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



@abc.get("/")
def test():
    return "test"

@abc.get("/get-students")
def all_students():
    return data

@abc.get("/all-student-names")
def get_all_names():
    "this api is for getting students names"
    return [ x["name"] for x in data ]

@abc.get("/all-student-city")
def get_all_city():
    return [ x["city"] for x in data ]

@abc.get("/all-students-with-name-a")
def get_all_city():
    return [ x["name"] for x in data if x["name"].startswith("A") or x["name"].startswith("a") ]

@abc.get("/get_by_id/{id:int}")
def get_student_by_id(id):
    for x in data:
        if x["id"] == id:
            return x
    return {
        "status": False,
        "message": "Id not found."
    }


@abc.get("/{key}")
def filter(key):
    return [ x[key] for x in data ]

@abc.get("/{name}/{city}")
def filter(name, city):
    return f"Hello {name}, welcome to {city}."

