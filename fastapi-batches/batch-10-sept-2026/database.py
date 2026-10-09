class StudentModel:

    def __init__(self, id, name, email, phone, city, state, password="Password@123"):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city
        self.state = state
        self.password = password

    def __repr__(self):
        return f"{self.id} - {self.name}"

data = []

data.append(StudentModel(
    id=1,
    name="Aarav Sharma",
    email="aarav.sharma@student.in",
    phone="+91 98765 43210",
    city="New Delhi",
    state="Delhi",
    password="Password@123"
))

data.append(StudentModel(
    id=2,
    name="Priya Patel",
    email="priya.patel@student.in",
    phone="+91 98234 56781",
    city="Ahmedabad",
    state="Gujarat",
    password="Password@123"
))

data.append(StudentModel(
    id=3,
    name="Rohan Mehta",
    email="rohan.mehta@student.in",
    phone="+91 97654 32109",
    city="Mumbai",
    state="Maharashtra",
    password="Password@123"
))

data.append(StudentModel(
    id=4,
    name="Ananya Iyer",
    email="ananya.iyer@student.in",
    phone="+91 98456 78901",
    city="Chennai",
    state="Tamil Nadu",
    password="Password@123"
))

data.append(StudentModel(
    id=5,
    name="Vikram Singh",
    email="vikram.singh@student.in",
    phone="+91 98123 45670",
    city="Jaipur",
    state="Rajasthan",
    password="Password@123"
))

data.append(StudentModel(
    id=6,
    name="Sneha Reddy",
    email="sneha.reddy@student.in",
    phone="+91 99087 65432",
    city="Hyderabad",
    state="Telangana",
    password="Password@123"
))

data.append(StudentModel(
    id=7,
    name="Arjun Nair",
    email="arjun.nair@student.in",
    phone="+91 97432 10987",
    city="Kochi",
    state="Kerala",
    password="Password@123"
))

data.append(StudentModel(
    id=8,
    name="Kavya Desai",
    email="kavya.desai@student.in",
    phone="+91 98321 09876",
    city="Pune",
    state="Maharashtra",
    password="Password@123"
))

data.append(StudentModel(
    id=9,
    name="Rahul Gupta",
    email="rahul.gupta@student.in",
    phone="+91 96543 21098",
    city="Lucknow",
    state="Uttar Pradesh",
    password="Password@123"
))

data.append(StudentModel(
    id=10,
    name="Ishita Banerjee",
    email="ishita.banerjee@student.in",
    phone="+91 93321 87654",
    city="Kolkata",
    state="West Bengal",
    password="Password@123"
))

data.append(StudentModel(
    id=11,
    name="Kabir Joshi",
    email="kabir.joshi@student.in",
    phone="+91 91234 56789",
    city="Bengaluru",
    state="Karnataka",
    password="Password@123"
))

data.append(StudentModel(
    id=12,
    name="Diya Sen",
    email="diya.sen@student.in",
    phone="+91 92345 67890",
    city="Guwahati",
    state="Assam",
    password="Password@123"
))

data.append(StudentModel(
    id=13,
    name="Aditya Verma",
    email="aditya.verma@student.in",
    phone="+91 93456 78901",
    city="Patna",
    state="Bihar",
    password="Password@123"
))

data.append(StudentModel(
    id=14,
    name="Meera Pillai",
    email="meera.pillai@student.in",
    phone="+91 94567 89012",
    city="Thiruvananthapuram",
    state="Kerala",
    password="Password@123"
))

data.append(StudentModel(
    id=15,
    name="Zoya Khan",
    email="zoya.khan@student.in",
    phone="+91 95678 90123",
    city="Bhopal",
    state="Madhya Pradesh",
    password="Password@123"
))

data.append(StudentModel(
    id=16,
    name="Karan Malhotra",
    email="karan.malhotra@student.in",
    phone="+91 96789 01234",
    city="Chandigarh",
    state="Punjab",
    password="Password@123"
))

data.append(StudentModel(
    id=17,
    name="Tanvi Kulkarni",
    email="tanvi.kulkarni@student.in",
    phone="+91 97890 12345",
    city="Nagpur",
    state="Maharashtra",
    password="Password@123"
))

data.append(StudentModel(
    id=18,
    name="Siddharth Rao",
    email="siddharth.rao@student.in",
    phone="+91 98901 23456",
    city="Visakhapatnam",
    state="Andhra Pradesh",
    password="Password@123"
))

data.append(StudentModel(
    id=19,
    name="Nisha Das",
    email="nisha.das@student.in",
    phone="+91 99012 34567",
    city="Bhubaneswar",
    state="Odisha",
    password="Password@123"
))

data.append(StudentModel(
    id=20,
    name="Varun Kapoor",
    email="varun.kapoor@student.in",
    phone="+91 90123 45678",
    city="Surat",
    state="Gujarat",
    password="Password@123"
))
