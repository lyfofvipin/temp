from . import app, render_template, flash
from flask_login import login_required, current_user

@app.route("/")
def home():
    return render_template("home.html", title = "Home")

@app.route("/about")
@login_required
def about():
    return "About Page."

@app.route("/test")
def test():
    return render_template("test.html", current_user=current_user)

