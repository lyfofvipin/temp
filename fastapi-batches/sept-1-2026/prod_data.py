class ProductModel:

    def __init__(self, id, title, category, price, stock, brand, is_active=True):
        self.id = id
        self.title = title
        self.category = category
        self.price = price
        self.stock = stock
        self.brand = brand
        self.is_active = is_active

    def __repr__(self):
        return f"{self.id} - {self.title}"

a = ProductModel(1, "test", 23, 23, 45, 46, 56)

data = []

products = [
    (1, "Wireless Bluetooth Headphones", "Electronics", 2999.00, 45, "Boat"),
    (2, "Ergonomic Office Chair", "Furniture", 8499.00, 12, "Green Soul"),
    (3, "Stainless Steel Water Bottle", "Home & Kitchen", 599.00, 150, "Milton"),
    (4, "Mechanical Gaming Keyboard", "Electronics", 4299.00, 25, "Redragon"),
    (5, "Running Shoes - Men", "Footwear", 2499.00, 30, "Puma"),
    (6, "Smart Fitness Band", "Electronics", 1999.00, 80, "Noise"),
    (7, "Cotton Casual Shirt", "Clothing", 1299.00, 60, "Allen Solly"),
    (8, "Ceramic Coffee Mug Set", "Home & Kitchen", 799.00, 40, "Clay Craft"),
    (9, "4K Ultra HD Smart TV 43-inch", "Electronics", 24999.00, 8, "Xiaomi"),
    (10, "Leather Laptop Backpack", "Bags", 3199.00, 20, "Wildcraft"),
    (11, "Analog Wrist Watch", "Accessories", 1899.00, 35, "Titan"),
    (12, "Non-Stick Cookware Set", "Home & Kitchen", 3499.00, 18, "Prestige"),
    (13, "Wireless Gaming Mouse", "Electronics", 1499.00, 50, "Logitech"),
    (14, "Denim Jeans - Slim Fit", "Clothing", 1999.00, 42, "Levi's"),
    (15, "Noise Cancelling Earbuds", "Electronics", 4999.00, 28, "Realme"),
]

for p in products:
    data.append(ProductModel(
        id=p[0],
        title=p[1],
        category=p[2],
        price=p[3],
        stock=p[4],
        brand=p[5]
    ))
