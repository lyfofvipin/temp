from flask import Flask, request, abort, render_template

app = Flask(__name__)


@app.route("/test")
def take_form_data():
    abort(401)
    return "Test"

@app.errorhandler(404)
def a(e):
    return render_template("a.html"), 404

@app.route("/b")
def b():
    return "B."
