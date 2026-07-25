from src import app, render_template, request, flash, redirect
from src.models import Post, db
from src import current_user, login_required

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "GET":
        return render_template("posts/create.html")
    
    if request.method == "POST":
        return request.form
        # title = request.form.get("title")
        # desc = request.form.get("description")
        # data_to_add = Post( title=title, description=desc,
        #                 user_id = current_user.id )
        # db.session.add(data_to_add)
        # db.session.commit()
        # flash("Post Added Done.")
        # return redirect("/")
