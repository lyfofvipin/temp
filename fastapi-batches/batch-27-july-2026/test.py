from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
def home():
    return "Hello This is Home Page."

@app.get("/blog")
def blog():
    return "Hello This is blog Page."

@app.get("/about")
def about():
    return "Hello This is about Page."

@app.get("/{name}")
def dynamic(name):
    return f"You Added {name} after profile."

@app.get("/{name}/{age}")
def detail(name, age):
    return f"{name} is {age} years old."
