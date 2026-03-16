from users import User, database, app, render_template


@app.route("/get_user_by_iddd/<int:id>")
def get_user_by_iddd(id):
    
    user_info = User.query.get(id)
    return render_template(
        "profile.html",
        name=user_info.name,
        username=user_info.username,
        email=user_info.email,
        profile_photo= user_info.profile_photo[7:]
    )
