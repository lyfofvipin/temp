from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/singup")
def take_form_data():
    return render_template("register.html", title = "Register")

@app.route("/data_validation", methods=["POST"])
def validate_data():
    username = request.form.get("username")
    mail = request.form.get("mail")
    password = request.form.get("password")

    if all([username, mail, password]):
        return render_template("data_valid.html", login=True)
    else:
        return render_template("data_valid.html", login = False)

@app.route("/login", methods=["GET", "POST"])
def login_func():
    if request.method == "GET":
        return render_template("login_page.html", title="Login")
    elif request.method == "POST":
        login_status = request.form.get("mail") == "abc@gmail.com" and request.form.get("password") == "123"
        return render_template("login_page.html", title="Login Verification", login=login_status)
