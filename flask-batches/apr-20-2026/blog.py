from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog_web.db"
database = SQLAlchemy(app)

class Posts( database.Model ):

    id = database.Column( database.Integer, primary_key = True )
    title = database.Column( database.String )
    description = database.Column( database.String )

with app.app_context():
    database.create_all()

@app.route("/")
def home():
    return render_template("blog_web/home.html")

@app.route("/about")
def about():
    return render_template("blog_web/about.html")

@app.route("/create")
def create():
    return render_template("blog_web/create.html")

@app.route("/write_post", methods=["POST"])
def write_post():
    a = Posts( title = request.form.get("title"), description = request.form.get("description"))
    database.session.add(a)
    database.session.commit()

    return render_template("blog_web/create.html")
