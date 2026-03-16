from . import app, render_template, request, url_for
from .models import User, database
from flask_login import login_required, current_user
import bcrypt


@app.route("/register")
def register():
    return render_template("user_register.html", title="Register Page")

@app.route("/validate_data", methods=["POST"])
def validate_data():
    name = request.form.get("name")
    email = request.form.get("mail")
    username = request.form.get("username")
    password = request.form.get("password")
    image = request.files.get("photo")

    if all((username, password, email)):
        data_to_dump = User(
            name = name,
            email = email,
            username = username,
            password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        )
        if image:
            photo_path = "profile_pics/" + username + ".png"
            image.save("static/" + photo_path)
            data_to_dump.profile_photo = photo_path

        database.session.add(data_to_dump)
        database.session.commit()

        return "User Created Done."
    else:
        return "You did not pass all the required values.", 409

@app.route("/get_user_by_id/<int:id>")
@login_required
def get_user_by_id(id):
    
    user_info = User.query.get(id)

    if str(user_info.id) != current_user.get_id():
        return "You are not allowed to see anyone else profile."

    return render_template(
        "profile.html",
        name=user_info.name,
        username=user_info.username,
        email=user_info.email,
        profile_photo= user_info.profile_photo[7:]
    )

@app.route("/get_user_by_username/<username>")
@login_required
def get_user_by_username(username):
    
    user_info = User.query.filter_by( username=username ).all()
    if user_info:
        user_info=user_info[0]

        if str(user_info.id) != current_user.get_id():
            return "You are not allowed to see anyone else profile."

        return render_template(
            "profile.html",
            name=user_info.name,
            username=user_info.username,
            email=user_info.email,
            profile_photo= user_info.profile_photo[7:]
        )
    else:
        return "User Not Found.", 409


@app.route("/delete_user_by_username/<username>")
@login_required
def delete_user_by_username(username):
    
    user_info = User.query.filter_by( username=username ).all()
    if user_info:
        user_info=user_info[0]

        if str(user_info.id) != current_user.get_id():
            return "You are not allowed to see anyone else profile."


        database.session.delete(user_info)
        database.session.commit()
        return "User deleted done."
    else:
        return "User Not Found.", 409


@app.route("/update_user_by_username/<username>", methods=["POST"])
@login_required
def update_user_by_username(username):
    
    user_info = User.query.filter_by(username = username).all()
    if user_info:
        user_info = user_info[0]

        if str(user_info.id) != current_user.get_id():
            return "You are not allowed to see anyone else profile."

        
        form_password = request.form.get("password")
        if form_password:
            if form_password.isnumeric():
                return "Your Password do not contain Alphabet and Number please type a combinations of both."
            user_info.password = form_password

        form_name = request.form.get("name")
        if form_name:
            user_info.name = form_name
        
        form_username = request.form.get("username")
        if form_username and form_username != user_info.username:
            validate_username = User.query.filter_by(username=form_username).all()
            if validate_username:
                return "This username is already Taken", 409
            else:
                user_info.username = form_username

        form_email = request.form.get("email")
        if form_email and form_email != user_info.email:
            validate_email = User.query.filter_by(email=form_email).all()
            if validate_email:
                return "Multiple Account with same ID are not allowed.", 409
            else:
                user_info.email = form_email
    
        photo = request.files.get("photo")
        if photo:
            path = f"static/profile_pics/{user_info.username}.png"
            user_info.profile_photo = path
            photo.save(path)

        database.session.add(user_info)
        database.session.commit()
        return "User Updated Done."
    else:
        return "User Not Found", 409

@app.route("/dummy")
def dummy_func():
    return f"{current_user.is_authenticated}"
