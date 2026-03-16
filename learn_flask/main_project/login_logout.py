from flask_login import login_user, logout_user
from . import app, render_template, request, redirect, url_for, flash
from .models import User
import bcrypt

@app.route("/login")
def login_func():
    return render_template("login.html")

@app.route("/validate_login", methods=["POST"])
def validate_login_func():
    user_in_db = User.query.filter_by( username = request.form.get("username") ).first()
    if user_in_db:
        if bcrypt.checkpw(request.form.get('password').encode(), hashed_password=user_in_db.password):
            login_user(user_in_db)
        else:
            return "Invalid Password.", 401
    else:
        return "User Not Found.", 409
    flash("Logged in successfully.")
    return redirect("/")

@app.route("/logout")
def logout_func():
    logout_user()
    flash("Logged Out successfully.")
    return redirect("/")
