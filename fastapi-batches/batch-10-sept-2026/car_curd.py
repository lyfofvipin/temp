class CarModel:

    def __init__(self, id, brand, model, year, color, registration_number,
                 owner_name, email, phone, city, state):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.registration_number = registration_number
        self.owner_name = owner_name
        self.email = email
        self.phone = phone
        self.city = city
        self.state = state

    def __repr__(self):
        return f"{self.id} - {self.brand} {self.model}"


data = []

data.append(CarModel(
    id=1,
    brand="Maruti Suzuki",
    model="Swift",
    year=2022,
    color="Red",
    registration_number="DEMO-0001",
    owner_name="Aarav Sharma",
    email="aarav.sharma@example.com",
    phone="+91 90000 00001",
    city="New Delhi",
    state="Delhi"
))

data.append(CarModel(
    id=2,
    brand="Hyundai",
    model="Creta",
    year=2023,
    color="White",
    registration_number="DEMO-0002",
    owner_name="Priya Patel",
    email="priya.patel@example.com",
    phone="+91 90000 00002",
    city="Ahmedabad",
    state="Gujarat"
))

data.append(CarModel(
    id=3,
    brand="Tata",
    model="Nexon",
    year=2024,
    color="Blue",
    registration_number="DEMO-0003",
    owner_name="Rohan Mehta",
    email="rohan.mehta@example.com",
    phone="+91 90000 00003",
    city="Mumbai",
    state="Maharashtra"
))

data.append(CarModel(
    id=4,
    brand="Mahindra",
    model="Scorpio",
    year=2021,
    color="Black",
    registration_number="DEMO-0004",
    owner_name="Ananya Iyer",
    email="ananya.iyer@example.com",
    phone="+91 90000 00004",
    city="Chennai",
    state="Tamil Nadu"
))

data.append(CarModel(
    id=5,
    brand="Honda",
    model="City",
    year=2022,
    color="Silver",
    registration_number="DEMO-0005",
    owner_name="Vikram Singh",
    email="vikram.singh@example.com",
    phone="+91 90000 00005",
    city="Jaipur",
    state="Rajasthan"
))

data.append(CarModel(
    id=6,
    brand="Toyota",
    model="Innova",
    year=2023,
    color="Grey",
    registration_number="DEMO-0006",
    owner_name="Sneha Reddy",
    email="sneha.reddy@example.com",
    phone="+91 90000 00006",
    city="Hyderabad",
    state="Telangana"
))

data.append(CarModel(
    id=7,
    brand="Kia",
    model="Seltos",
    year=2024,
    color="Green",
    registration_number="DEMO-0007",
    owner_name="Arjun Nair",
    email="arjun.nair@example.com",
    phone="+91 90000 00007",
    city="Kochi",
    state="Kerala"
))

data.append(CarModel(
    id=8,
    brand="Tata",
    model="Punch",
    year=2023,
    color="Orange",
    registration_number="DEMO-0008",
    owner_name="Kavya Desai",
    email="kavya.desai@example.com",
    phone="+91 90000 00008",
    city="Pune",
    state="Maharashtra"
))

data.append(CarModel(
    id=9,
    brand="Maruti Suzuki",
    model="Baleno",
    year=2022,
    color="Blue",
    registration_number="DEMO-0009",
    owner_name="Rahul Gupta",
    email="rahul.gupta@example.com",
    phone="+91 90000 00009",
    city="Lucknow",
    state="Uttar Pradesh"
))

data.append(CarModel(
    id=10,
    brand="Hyundai",
    model="i20",
    year=2021,
    color="White",
    registration_number="DEMO-0010",
    owner_name="Ishita Banerjee",
    email="ishita.banerjee@example.com",
    phone="+91 90000 00010",
    city="Kolkata",
    state="West Bengal"
))

data.append(CarModel(
    id=11,
    brand="Toyota",
    model="Fortuner",
    year=2024,
    color="Black",
    registration_number="DEMO-0011",
    owner_name="Kabir Joshi",
    email="kabir.joshi@example.com",
    phone="+91 90000 00011",
    city="Bengaluru",
    state="Karnataka"
))

data.append(CarModel(
    id=12,
    brand="Renault",
    model="Kwid",
    year=2020,
    color="Red",
    registration_number="DEMO-0012",
    owner_name="Diya Sen",
    email="diya.sen@example.com",
    phone="+91 90000 00012",
    city="Guwahati",
    state="Assam"
))

data.append(CarModel(
    id=13,
    brand="Mahindra",
    model="Thar",
    year=2023,
    color="Green",
    registration_number="DEMO-0013",
    owner_name="Aditya Verma",
    email="aditya.verma@example.com",
    phone="+91 90000 00013",
    city="Patna",
    state="Bihar"
))

data.append(CarModel(
    id=14,
    brand="Honda",
    model="Amaze",
    year=2022,
    color="Silver",
    registration_number="DEMO-0014",
    owner_name="Meera Pillai",
    email="meera.pillai@example.com",
    phone="+91 90000 00014",
    city="Thiruvananthapuram",
    state="Kerala"
))

data.append(CarModel(
    id=15,
    brand="Tata",
    model="Harrier",
    year=2024,
    color="Grey",
    registration_number="DEMO-0015",
    owner_name="Zoya Khan",
    email="zoya.khan@example.com",
    phone="+91 90000 00015",
    city="Bhopal",
    state="Madhya Pradesh"
))

data.append(CarModel(
    id=16,
    brand="Volkswagen",
    model="Virtus",
    year=2023,
    color="White",
    registration_number="DEMO-0016",
    owner_name="Karan Malhotra",
    email="karan.malhotra@example.com",
    phone="+91 90000 00016",
    city="Chandigarh",
    state="Punjab"
))

data.append(CarModel(
    id=17,
    brand="Skoda",
    model="Slavia",
    year=2022,
    color="Blue",
    registration_number="DEMO-0017",
    owner_name="Tanvi Kulkarni",
    email="tanvi.kulkarni@example.com",
    phone="+91 90000 00017",
    city="Nagpur",
    state="Maharashtra"
))

data.append(CarModel(
    id=18,
    brand="MG",
    model="Hector",
    year=2024,
    color="Black",
    registration_number="DEMO-0018",
    owner_name="Siddharth Rao",
    email="siddharth.rao@example.com",
    phone="+91 90000 00018",
    city="Visakhapatnam",
    state="Andhra Pradesh"
))

data.append(CarModel(
    id=19,
    brand="Kia",
    model="Sonet",
    year=2023,
    color="Silver",
    registration_number="DEMO-0019",
    owner_name="Nisha Das",
    email="nisha.das@example.com",
    phone="+91 90000 00019",
    city="Bhubaneswar",
    state="Odisha"
))

data.append(CarModel(
    id=20,
    brand="Maruti Suzuki",
    model="Brezza",
    year=2024,
    color="Red",
    registration_number="DEMO-0020",
    owner_name="Varun Kapoor",
    email="varun.kapoor@example.com",
    phone="+91 90000 00020",
    city="Surat",
    state="Gujarat"
))


from fastapi import FastAPI, status, Response

app = FastAPI()


@app.get("/")
def home():
    return "this is homepage"


@app.get("/health")
def health():
    return {"status": True}

@app.get("/cars")
def all_cars():
    return {"status": True, "data": data, "message": "Cars fetched successfully"}

@app.get("/car_by_id/{id}")
def car_by_id(id:int, rsp: Response):

    for x in data:
        if x.id == id:
            return {"status": True, "data": x, "message": "Car fetched successfully"}

    rsp.status_code = status.HTTP_404_NOT_FOUND
    return {"status": False, "message": "Car id not found."}


@app.post("/create_car")
def create_car(car_data: dict, response:Response):

    if not all([ car_data.get("brand"), 
            car_data.get("model"),
            car_data.get("color"),
            car_data.get("registration_number"),
            car_data.get("owner_name"),
            car_data.get("email"),
            car_data.get("phone"),
            car_data.get("city"),
            car_data.get("state"),
            car_data.get("year")]):

        response.status_code = status.HTTP_409_CONFLICT
        return {"status": False, "message": "You are missing one of the values."}    

    data.append(
        CarModel(
            id=len(data) + 1,
            brand=car_data["brand"], model=car_data["model"],
            color=car_data["color"], registration_number=car_data["registration_number"],
            owner_name=car_data["owner_name"], email=car_data["email"],
            phone=car_data["phone"],
            city=car_data["city"],
            state=car_data["state"],
            year=car_data["year"],
        )
    )

    return {"status": True, "message": "Car Added successfully"}


@app.patch("/update_car{id}")
def update_car(id:int, car_data: dict, response: Response):

    if not any( [car_data.get("brand"), car_data.get("model"), car_data.get("color"),
            car_data.get("registration_number"),
            car_data.get("owner_name"),
            car_data.get("email"),
            car_data.get("phone"),
            car_data.get("city"),
            car_data.get("state"),
            car_data.get("year")]):

        response.status_code = status.HTTP_409_CONFLICT
        return {"status": False, "message": "Enter 1 value to update."}    

    for x in data:
        if x.id == id:

            if car_data.get("brand"): x.brand = car_data["brand"]
            if car_data.get("model"): x.model = car_data["model"]
            if car_data.get("color"): x.color = car_data["color"]      
            if car_data.get("owner_name"): x.owner_name = car_data["owner_name"]
            if car_data.get("phone"): x.phone = car_data["phone"]
            if car_data.get("city"): x.city = car_data["city"]
            if car_data.get("state"): x.state = car_data["state"]
            if car_data.get("year"): x.year = car_data["year"]

            return {"status": True, "message": "Car updated."}

    response.status_code = status.HTTP_404_NOT_FOUND
    return {"status": False, "message": "Id not found"}

@app.delete("/delete/")
def delete_car(id:int, response: Response):
    for x in data:
        if x.id == id:
            data.remove(x)
            return {"status": True, "message": "data deleted done"}

    response.status_code = status.HTTP_404_NOT_FOUND
    return {"status": False, "message": "Id not found"}

    