from src import app, render_template, login_required, make_response
from src import request, flash, redirect, abort, login_user, url_for, current_user
from src.models import db, Users

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/details")
def ab():
    return render_template("about.html")

@app.route("/contact")
@login_required
def contact():
    resp = make_response(render_template("contact.html"))
    resp.set_cookie("Vipin", "Test")
    return resp

@app.route("/profile")
@login_required
def profile():
    data = Users.query.all()
    return render_template("profile.html", fe_data = data)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        user_mail = request.form.get("email")
        user_password = request.form.get("password")

        database_data = Users.query.filter( Users.email == user_mail ).first()
        if not database_data:
            flash("Username Not Found.", "error")
            return redirect("/")

        if database_data.password == user_password:
            login_user(database_data)
            flash("Login Successful.")
            return redirect("/")
        else:
            abort(401)

@app.errorhandler(401)
def handle404(error):
    return render_template("handle404_error.html")

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


        file = request.files["photo"]
        if file:
            image_path = f'static/{request.form.get("email")}.png'
            file.save(image_path)
            a.photo = f"{request.form.get("email")}.png"
        else:
            a.photo = "default.png"

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
@login_required
def list_students():
    data = Users.query.all()
    return render_template("list_students.html", fe_data = data)

@app.route("/test")
def test():
    print( url_for('update_student', student_id=1) )
    return "test"

@app.route("/list_student/<int:student_id>", methods=["GET", 'POST'])
@login_required
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

    return render_template("update_student.html", data = data)
