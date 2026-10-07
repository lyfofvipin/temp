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
        return f"User({self.id}): {self.name}"


class ProductModel:

    def __init__(self, id, title, category, price, stock, brand):
        self.id = id
        self.title = title
        self.category = category
        self.price = price
        self.stock = stock
        self.brand = brand

    def __repr__(self):
        return f"Product({self.id}): {self.title} - ₹{self.price}"

class OrderModel:

    def __init__(self, id, user_id, product_id, quantity, payment_mode="UPI", status="COMPLETED"):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.payment_mode = payment_mode
        self.status = status

    def __repr__(self):
        return f"Order({self.id}): User {self.user_id} bought Product {self.product_id} (Qty: {self.quantity})"


# ==========================================
# DATA DUMP
# ==========================================

users_data = [
    StudentModel(1, "Aarav Sharma", "aarav.sharma@student.in", "+91 98765 43210", "New Delhi", "Delhi"),
    StudentModel(2, "Priya Patel", "priya.patel@student.in", "+91 98234 56781", "Ahmedabad", "Gujarat"),
    StudentModel(3, "Rohan Mehta", "rohan.mehta@student.in", "+91 97654 32109", "Mumbai", "Maharashtra"),
    StudentModel(4, "Ananya Iyer", "ananya.iyer@student.in", "+91 98456 78901", "Chennai", "Tamil Nadu"),
    StudentModel(5, "Vikram Singh", "vikram.singh@student.in", "+91 98123 45670", "Jaipur", "Rajasthan"),
]

products_data = [
    ProductModel(101, "Wireless Bluetooth Headphones", "Electronics", 2999.00, 45, "Boat"),
    ProductModel(102, "Ergonomic Office Chair", "Furniture", 8499.00, 12, "Green Soul"),
    ProductModel(103, "Stainless Steel Water Bottle", "Home & Kitchen", 599.00, 150, "Milton"),
    ProductModel(104, "Mechanical Gaming Keyboard", "Electronics", 4299.00, 25, "Redragon"),
    ProductModel(105, "Running Shoes - Men", "Footwear", 2499.00, 30, "Puma"),
]

orders_data = [
    OrderModel(id=1001, user_id=1, product_id=101, quantity=1, payment_mode="UPI"),
    OrderModel(id=1002, user_id=1, product_id=103, quantity=2, payment_mode="Credit Card"),
    OrderModel(id=1003, user_id=2, product_id=102, quantity=1, payment_mode="Net Banking"),
    OrderModel(id=1004, user_id=3, product_id=104, quantity=1, payment_mode="UPI"),
    OrderModel(id=1005, user_id=3, product_id=105, quantity=1, payment_mode="COD"),
    OrderModel(id=1006, user_id=5, product_id=101, quantity=2, payment_mode="UPI"),
]
