from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users_profile.db"
app.secret_key = "asdfhasgfsajdfoi34y8734y87h98dsijfoij2e983hj497fhuoinuoi" #notsecret
login_manager = LoginManager(app)

from . import users
from . import login_logout
from . import baisc
