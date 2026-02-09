from flask import Flask, render_template

app = Flask(__name__)


@app.route('/a')
def a():
    return render_template("a.html", title="A")

@app.route('/b')
def b():
    return render_template("b.html")


@app.route('/c')
def c():
    return render_template("c.html")


@app.route('/d')
def d():
    return render_template("d.html")


@app.route('/e')
def e():
    return render_template("e.html")
