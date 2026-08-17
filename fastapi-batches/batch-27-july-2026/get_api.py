data = [
    {
        "id": 1,
        "name": "Aarav Sharma",
        "email": "aarav.sharma@student.in",
        "phone": "+91 98765 43210",
        "city": "Ahmedabad",
        "state": "Delhi",
        "course": "Full Stack Python",
        "batch": "PY-2025-A",
        "age": 22,
        "gender": "Male",
        "enrollment_date": "2025-01-12",
        "status": "active",
        "score": 88.5
    },
    {
        "id": 2,
        "name": "Priya Patel",
        "email": "priya.patel@student.in",
        "phone": "+91 98234 56781",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "course": "MERN Stack",
        "batch": "ME-2025-B",
        "age": 21,
        "gender": "Female",
        "enrollment_date": "2025-01-18",
        "status": "active",
        "score": 91.2
    },
    {
        "id": 3,
        "name": "Rohan Mehta",
        "email": "rohan.mehta@student.in",
        "phone": "+91 97654 32109",
        "city": "Mumbai",
        "state": "Maharashtra",
        "course": "Java Full Stack",
        "batch": "JV-2025-A",
        "age": 23,
        "gender": "Male",
        "enrollment_date": "2025-02-02",
        "status": "inactive",
        "score": 79
    },
    {
        "id": 4,
        "name": "Ananya Iyer",
        "email": "ananya.iyer@student.in",
        "phone": "+91 98456 78901",
        "city": "Mumbai",
        "state": "Tamil Nadu",
        "course": "AIML",
        "batch": "AI-2025-C",
        "age": 20,
        "gender": "Female",
        "enrollment_date": "2025-02-08",
        "status": "inactive",
        "score": 94.3
    },
    {
        "id": 5,
        "name": "Vikram Singh",
        "email": "vikram.singh@student.in",
        "phone": "+91 98123 45670",
        "city": "Jaipur",
        "state": "Rajasthan",
        "course": "DevOps",
        "batch": "DO-2025-A",
        "age": 24,
        "gender": "Male",
        "enrollment_date": "2025-02-14",
        "status": "inactive",
        "score": 72.5
    },
    {
        "id": 6,
        "name": "Sneha Reddy",
        "email": "sneha.reddy@student.in",
        "phone": "+91 99087 65432",
        "city": "Hyderabad",
        "state": "Telangana",
        "course": "Full Stack Python",
        "batch": "PY-2025-B",
        "age": 22,
        "gender": "Female",
        "enrollment_date": "2025-02-20",
        "status": "active",
        "score": 86.7
    },
    {
        "id": 7,
        "name": "Arjun Nair",
        "email": "arjun.nair@student.in",
        "phone": "+91 97432 10987",
        "city": "Kochi",
        "state": "Kerala",
        "course": "MERN Stack",
        "batch": "ME-2025-A",
        "age": 21,
        "gender": "Male",
        "enrollment_date": "2025-03-01",
        "status": "active",
        "score": 83.4
    },
    {
        "id": 8,
        "name": "Kavya Desai",
        "email": "kavya.desai@student.in",
        "phone": "+91 98321 09876",
        "city": "Pune",
        "state": "Maharashtra",
        "course": "Manual QA",
        "batch": "QA-2025-A",
        "age": 23,
        "gender": "Female",
        "enrollment_date": "2025-03-05",
        "status": "active",
        "score": 90.1
    },
    {
        "id": 9,
        "name": "Rahul Gupta",
        "email": "rahul.gupta@student.in",
        "phone": "+91 96543 21098",
        "city": "Lucknow",
        "state": "Uttar Pradesh",
        "course": "Java Full Stack",
        "batch": "JV-2025-B",
        "age": 22,
        "gender": "Male",
        "enrollment_date": "2025-03-10",
        "status": "inactive",
        "score": 68.9
    },
    {
        "id": 10,
        "name": "Ishita Banerjee",
        "email": "ishita.banerjee@student.in",
        "phone": "+91 93321 87654",
        "city": "Kolkata",
        "state": "West Bengal",
        "course": "AIML",
        "batch": "AI-2025-A",
        "age": 20,
        "gender": "Female",
        "enrollment_date": "2025-03-15",
        "status": "active",
        "score": 92.8
    }
]

from fastapi import FastAPI

app = FastAPI()

@app.get("/name")
def name():
    return [ x["name"] for x in data ]

@app.get("/email")
def email():
    return [ x["email"] for x in data ]

@app.get("/phone")
def phone():
    return [ x["phone"] for x in data ]

@app.get("/user/{id}")
def id(id:int):
    for x in data:
        if x["id"] == int(id):
            return x
    return "Data Not Found"

@app.get("/{city}/{status}")
def id(city:str, status:str):
    data_to_return = []
    for x in data:
        if x["city"] == city and x["status"] == status:
            data_to_return.append(x)
    return data_to_return


@app.get("/get_user_based_on_city_or_status")
def id(city:str, status:str):
    data_to_return = []
    for x in data:
        if x["city"] == city and x["status"] == status:
            data_to_return.append(x)
    return data_to_return
