### 1. Database Model & Mock Data (`database.py`)

```python
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
        return f"{self.id} - {self.title} (₹{self.price})"


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

```

---

### 2. Practice Questions for Students

#### **Basic CRUD (Warm-Up)**

1. **GET `/products**`: Write an endpoint to retrieve all products.
2. **GET `/products/{id}**`: Write an endpoint to find a product by its ID. Return a `404`-style custom dictionary if the product is not found.
3. **POST `/products/add**`: Write an endpoint to create a new product. Auto-increment the ID based on existing list length.
4. **DELETE `/products/{id}**`: Write an endpoint to remove a product by ID. Handle the case where the product does not exist.
5. **PUT `/products/{id}**`: Write an endpoint that allows updating `price`, `stock`, or `title`. Preserve existing values if fields are not provided.

#### **Intermediate Logic (Filtering & Queries)**

6. **GET `/products/category/{category_name}**`: Write an endpoint to filter and return all products belonging to a specific category (e.g., `"Electronics"`).
7. **GET `/products/search?keyword=...**`: Create a query parameter endpoint to search for products whose title contains the keyword (case-insensitive).
8. **PATCH `/products/{id}/stock**`: Write an endpoint that takes an `id` and a `quantity` parameter to increase or decrease the stock count of a product.

#### **Advanced Logic (Business Use Cases)**

9. **GET `/products/out-of-stock**`: Write an endpoint that lists products where `stock == 0`.
10. **PATCH `/products/{id}/toggle-status**`: Write an endpoint that flips the `is_active` boolean value (`True` $\rightarrow$ `False` or `False` $\rightarrow$ `True`).