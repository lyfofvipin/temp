from run import app
from src import LoginManager, flash, redirect, logout_user, request, render_template, abort, login_user
from src.models import Users

lm = LoginManager(app)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logout Done")
    return redirect("/")


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        user_mail = request.form.get("email")
        user_password = request.form.get("password")

        database_data = Users.query.filter( Users.email == user_mail ).first()
        if not database_data:
            flash("Username Not Found.", "error")
            return redirect("/")

        if database_data.password == user_password:
            login_user(database_data)
            flash("Login Successful.")
            return redirect("/")
        else:
            abort(401)

@lm.user_loader
def user_fetch(id):
    return Users.query.get(int(id))
    # return db.Query.get(Users, int(id))
