from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello</h1>
    """

@app.route("/test")
def test():
  return [
    {
      "fullname": "Aarav Sharma",
      "email": "aarav.sharma@example.com",
      "username": "aarav123",
      "password": "password123",
      "is_active": True,
      "confirm_password": "password123"
    }
  ]


@app.route("/get_type_api")
def posttypeapi():
  a = {
     "status" : "success"
  }
  a.update(request.args)
  return a


@app.route("/post_type_api", methods=["post"])
def posttypeapi_parm():
  a = {
     "status" : "success"
  }
  a.update(request.form)
  return a

