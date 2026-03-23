from flask import Flask
from flask import url_for

test = Flask( __name__ )

# home/vipikuma/my_data/temp/python_prec

# Routes
@test.route("/<path:a>")
def test_str_route(a):
    return a

@test.route("/")
def dummy():
    return url_for("login_func")

@test.route("/about")
def about_func():
    return "Hi I am about function."

@test.route("/blog")
def blog_func():
    return "Hi I am blog function."

@test.route("/signup")
def login_func():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signup</title>
</head>
<body>
    <b>This is the signup Page.</b>
</body>
</html>
'''
