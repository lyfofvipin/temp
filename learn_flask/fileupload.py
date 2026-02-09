from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/test")
def take_form_data():
    return render_template("fileupload/file_upload.html", title = "File Upload.")


@app.route("/file_Save", methods = ["POST"])
def validate_data():

    file = request.files["file_to_upload"]
    file.save("static/" + file.filename)
    return "Done"
