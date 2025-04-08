from src import app

@app.route("/")
def home():
    return "Hi I am home."

@app.route("/about")
def about():
    return "Hi I am About."

