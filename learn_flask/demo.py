from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def hello():
    return f"""<h1>Hello, World!</h1>
<a href="{url_for('about_func')}" >About</a><br>
<a href="{url_for('greet', name="vipin")}" >Greet Url</a><br>
<a href="{url_for('vote_validation', age="23")}" >AGE</a>
"""

@app.route("/about")
def about_func():
    return "<h2>This is about page</h2>"


@app.route("/greet/<name>")
def greet(name):
    return f"""
<h1>Hi {name}</h1>
This is test website.
"""

@app.route("/age/<int:age>")
def vote_validation(age):
    if age > 18:
        return """
<h4 style="color:green" >Yes You Can Vote</h4>
"""
    else:
        return """
<h4 style="color:red" >No You Can not Vote</h4>
"""

@app.route("/path/<path:abc>")
def learn_path(abc):
    return abc


@app.route("/test_urls")
def learn_url_for():
    return url_for('learn_path', abc="/home/vipikuma/my_data/temp/learn_flask")

