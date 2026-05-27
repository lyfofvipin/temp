from flask import Flask
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user
from flask_login import UserMixin, login_required
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import url_for
from flask import flash
from flask import make_response

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///abc.db"
app.secret_key = "sahbd283jend03483nucndc3fr93834nusncdwi3948jf934" #notsecret
