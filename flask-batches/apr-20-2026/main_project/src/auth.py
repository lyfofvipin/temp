from run import app
from src import LoginManager, flash, redirect, logout_user
from src.models import Users

lm = LoginManager(app)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logout Done")
    return redirect("/")


@lm.user_loader
def user_fetch(id):
    return Users.query.get(int(id))
    # return db.Query.get(Users, int(id))
