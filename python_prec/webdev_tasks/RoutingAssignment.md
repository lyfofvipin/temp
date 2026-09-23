
---

# Routing Assignment

### **The App Code Setup**

Analyze the FastAPI application below. Pay close attention to the **order of the routes** and the **path parameters / converters** used.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_route():
    return "This is a home page route"

@app.get("/test")
def test_route():
    return "This is a test page route"

@app.get("/about")
def about_route():
    return "This is an about page route"

@app.get("/demo")
def demo_route():
    return "This is a demo page route"

@app.get("/{data}")
def single_param(data):
    return f"You passed {data} value."

@app.get("/{name}/{city}")
def double_param(name, city):
    return f"You passed {name} and {city} value."

@app.get("/{data:path}")
def path_param(data):
    return f"You passed {data} with / values."

```

---

### **Part 1: Predict the Route & Response (MCQ / Guessing)**

Without running the code, look at the request URL provided below and answer:

1. **Which route function handles it?**
2. **What exact response string does it return?**

#### **Static vs. Single Dynamic Routes**

1. `GET /`
2. `GET /test`
3. `GET /about`
4. `GET /demo`
5. `GET /rahul`
6. `GET /contact`

#### **Multi-Segment & Parameter Priority**

7. `GET /rahul/delhi`
8. `GET /demo/jaipur`
9. `GET /test/pune`
10. `GET /a/b`
11. `GET /john/new-york`
12. `GET /vipin/`

#### **Deep Paths & The `:path` Converter**

13. `GET /a/b/c`
14. `GET /about/mumbai`
15. `GET /first/second/third`
16. `GET /demo/profile/settings`
17. `GET /foo/bar/baz/qux`
18. `GET /test/details/extra`
19. `GET //mumbai`
20. `GET /users/dashboard/analytics/reports`

---

### **Part 2: Code-Writing Challenge**

For this section, you are given specific client requirements/routes. **Write the FastAPI code (decorator + function)** that can correctly handle each request scenario.

1. Create a route that handles a static URL for a contact page (`/contact`).
2. Create a route that captures a single product ID parameter from the URL (e.g., `/products/{product_id}`).
3. Create a route that captures both a category name and an item name (e.g., `/shop/{category}/{item}`).
4. Create a route that handles multi-segment file paths using the path converter (e.g., `/files/{filepath:path}`).
5. Create a static route for a user profile page (`/profile`).
6. Create a dynamic route that accepts a username (e.g., `/user/{username}`).
7. Create a route that captures a year and a month in the URL path (e.g., `/archive/{year}/{month}`).
8. Create a route that can capture any deeply nested document path (e.g., `/docs/{doc_path:path}`).
9. Create a static route for a terms and conditions page (`/terms`).
10. Create a dynamic route that accepts an order ID and returns a confirmation message containing that order ID.