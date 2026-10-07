from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    return "Thi is a home page route"

@app.get("/test")
def test():
    return "Thi is a test page route"

@app.get("/about")
def test():
    return "Thi is a about page route"

@app.get("/demo")
def test():
    return "Thi is a demo page route"

@app.get("/{data}")
def test(data):
    return f"You passed {data} value."

@app.get("/{name}/{city}")
def test(name, city):
    return f"You passe {name} and {city} value."

@app.get("/{data:path}")
def test(data):
    return f"You passed {data} with / values."

