from flask import Flask
from flask import render_template

app = Flask(__name__)

# test_path/
# "home/vipikuma/my_data/temp/flask-batches/apr-20-2026"
# render_template

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test_int/<int:a>")
def test_int(a):
    return str(a)

@app.route("/test_float/<float:a>")
def test_float(a):
    return str(a)

@app.route("/test_path/<path:a>")
def test_path(a):
    return str(a)

@app.route("/<xyx>/<pqr>")
def xyz_test(xyx, pqr):
    return f"Value of var is {xyx}, {pqr}"

@app.route("/profile/<xyz>")
def prfile(xyz):
    return f"Value of var is {xyz}"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/services")
def services():
    return "Our Services"

