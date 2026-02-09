from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vipin.db'

db = SQLAlchemy(app)

class Mytable(db.Model):
    pr_key = db.Column(db.Integer, primary_key=True)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# u1 = User( is_admin = True, username = "u5", email="u5", password="1234" )
# u2 = User( is_admin = True, username = "u6", email="u6", password="1234" )
# u3 = User( is_admin = True, username = "u7", email="u7", password="1234" )

with app.app_context():
    db.create_all()
    # db.session.add(u1)
    # db.session.add(u2)
    # db.session.add(u3)
    # db.session.commit()







