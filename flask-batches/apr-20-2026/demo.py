from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///abc.db"

db = SQLAlchemy( app )

class Users( db.Model ):

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String, nullable = False  )
    email = db.Column( db.String, nullable = False, unique = True )
    password = db.Column( db.String, nullable = False  )

with app.app_context():
    db.create_all()

print(app.config)