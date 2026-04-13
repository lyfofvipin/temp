from flask import Flask
from flask import url_for
from flask import render_template
from flask import request


test = Flask( __name__ )

# home/vipikuma/my_data/temp/python_prec

# Routes
# http://localhost:5000/?name=vipin&age=35&city=Jaipur
@test.route("/")
def dummy():
    return render_template("homepage.html")

@test.route("/about")
def about_func():
    return render_template("abouttttt.html")

@test.route("/blog")
def blog_func():
    return render_template("folder1/blog.html")

@test.route("/signup")
def login_func():
    return render_template("signup.html")

@test.route("/test_args")
def test_args():
    return request.args

@test.route("/test_form", methods=["POST", "GET"])
def test_form():
    return request.form

@test.route("/profile")
def profile():
    return render_template("profile.html", b="vipin")

