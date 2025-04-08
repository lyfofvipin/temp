from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///manisha.db"

db = SQLAlchemy(app)


class User( db.Model ):

    id  = db.Column(db.Integer, primary_key=True)
    amount  = db.Column(db.Float)
    name  = db.Column(db.String)


class Client( db.Model ):

    client_id  = db.Column(db.Integer, primary_key=True)
    amount  = db.Column(db.Float)
    name  = db.Column(db.String)

user1 = User( name = "Vipin", amount = 45.34 )

user2 = User()
user2.name = "Vikas"
user2.amount = 345.34


with app.app_context():
    db.create_all()
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

