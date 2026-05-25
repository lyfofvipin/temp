from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
database = SQLAlchemy(app)

class Movie( database.Model ):

    id = database.Column( database.Integer, primary_key = True )
    name = database.Column( database.String )
    description = database.Column( database.String )
    rating = database.Column( database.String )
    duration = database.Column( database.String )

with app.app_context():
    database.create_all()

@app.route("/")
def home():
    return render_template("movie/home.html")

@app.route("/about")
def about():
    return render_template("movie/about.html")

@app.route("/create")
def create():
    return render_template("movie/create.html")

@app.route("/write_post", methods=["POST"])
def write_post():
    a = Posts( title = request.form.get("title"), description = request.form.get("description"))
    database.session.add(a)
    database.session.commit()

    return render_template("movie/create.html")

@app.route("/show_blog")
def show_blog():
    all_blog_data = Posts.query.all()
    return render_template("movie/show_blog.html", data = all_blog_data)

@app.route("/display/<int:number>")
def display_blog(number):
    blog = Posts.query.filter( Posts.id == number ).first()
    if not blog:
        return "Blog With Above Id not found."
    return render_template("movie/display_blog.html", x = blog)

@app.route("/delete/<int:number>")
def delete(number):
    blog = Posts.query.filter( Posts.id == number ).first()
    if not blog:
        return "Blog With Above Id not found."

    database.session.delete(blog)
    database.session.commit()
    return "Blog Deleted successfully."

@app.route("/update_vlog/<int:id>")
def update(id):

    blog = Posts.query.filter( Posts.id == id ).first()
    if not blog:
        return f"Blog with ID {id} not found."

    if not request.args.get("title") and not request.args.get("description"):
        return render_template("movie/update.html", id=id)
    else:
        if request.args.get("title"):
            blog.title = request.args.get("title")

        if request.args.get("description"):
            blog.description = request.args.get("description")
        
    database.session.add(blog)
    database.session.commit()
    return "Blog Updated Successfully."

