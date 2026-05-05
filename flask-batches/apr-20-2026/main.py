from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///abc.db"

db = SQLAlchemy( app )

class Users( db.Model ):

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String, nullable = False  )
    email = db.Column( db.String, nullable = False, unique = True )
    password = db.Column( db.String, nullable = False  )
    collage = db.Column( db.String )

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/profile")
def profile():
    data = Users.query.all()
    return render_template("profile.html", fe_data = data)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/form_args")
def form_args():
    return request.args

@app.route("/form_form", methods=["POST"])
def form_form():
    with open("test.text", "w") as file:
        file.write(str(request.form))
    return "Operation Completed Done."

@app.route("/register", methods=["GET", 'POST'])
def register():
    if request.method == "POST":

        a = Users(
            name = request.form.get("name"),
            email = request.form.get("email"),
            password = request.form.get("password")
        )

        db.session.add(a)
        db.session.commit()
        return "User Created Successfully."

    return render_template("register.html")

@app.route("/search")
def search():
    if request.args:
        collage_name = request.args["collage_name"]
        data = Users.query.filter( Users.collage == collage_name ).all()
        return render_template("search_collage.html", fe_data = data)

    return render_template("search_collage.html")

@app.route("/list_students")
def list_students():
    data = Users.query.all()
    return render_template("list_students.html", fe_data = data)

@app.route("/update_student/<int:student_id>", methods=["GET", 'POST'])
def update_student(student_id):

    data = Users.query.filter( Users.id == student_id ).first()
    if not data:
        return f"Student Not Found with id: {student_id}."

    if request.method == "POST":

        if request.form.get("name"):
            data.name = request.form.get("name")

        if request.form.get("email"):
            data.email = request.form.get("email")

        if request.form.get("password"):
            data.password = request.form.get("password")

        if request.form.get("collage"):
            data.collage = request.form.get("collage")

        db.session.add(data)
        db.session.commit()
        return "User Updated Successfully."

    return render_template("update_student.html", student_id = student_id)
