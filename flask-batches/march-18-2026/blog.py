from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
database = SQLAlchemy(app)

class Item( database.Model ):

    id = database.Column( database.Integer, primary_key = True )
    name = database.Column( database.String )
    description = database.Column( database.String )
    rating = database.Column( database.String )
    duration = database.Column( database.String )

with app.app_context():
    database.create_all()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add_movie", methods=["POST"])
def add_movie():

    # obj = Movie( name = request.form.get('name'), description = request.form.get('description'), rating = request.form.get('rating'), duration = request.form.get('duration'))

    obj = Movie(
        name = request.form.get('name'),
        description = request.form.get('description'),
        rating = request.form.get('rating'),
        duration = request.form.get('duration')
    )

    database.session.add(obj)
    database.session.commit()

    return render_template("add.html")

@app.route("/show_movies")
def show_movie():
    all_movie_data = Movie.query.all()
    return render_template("show_movie.html", data = all_movie_data)

@app.route("/details/<int:id>")
def details(id):
    movie = Movie.query.filter( Movie.id == id ).first()
    if not movie:
        return "Movie With Above Id not found."
    return render_template("details.html", x = movie)

@app.route("/delete/<int:number>")
def delete(number):
    movie = Movie.query.filter( Movie.id == number ).first()
    if not movie:
        return "Movie With Above Id not found."

    database.session.delete(movie)
    database.session.commit()
    return "Move Deleted successfully."

@app.route("/update_movie/<int:id>")
def update(id):

    movie = Movie.query.filter( Movie.id == id ).first()
    if not movie:
        return f"movie with ID {id} not found."

    if any(request.form.values() ):
        return render_template("update.html", movie = movie)
    else:
        if request.args.get("name"):
            movie.name = request.args.get("name")

        if request.args.get("description"):
            movie.description = request.args.get("description")

        if request.args.get("rating"):
            movie.rating = request.args.get("rating")

        if request.args.get("duration"):
            movie.duration = request.args.get("duration")

    database.session.add(movie)
    database.session.commit()
    return "Movie Updated Successfully."

