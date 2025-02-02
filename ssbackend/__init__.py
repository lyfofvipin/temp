from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.database'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.String(50), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    confirm_password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"< id = {self.id}, username = {self.username} >"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(50), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"< id = {self.id}, username = {self.username}, title = {self.title} >"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(50))
    comment_content = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"< id = {self.id}, username = {self.username}, post_id = {self.post_id} >"

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(50))
    like_status = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"< id = {self.id}, username = {self.username}, post_id = {self.post_id} >"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_username = db.Column(db.String(50), nullable=False)
    receiver_username = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"< id = {self.id}, username = {self.sender_username}, receiver_username = {self.receiver_username} >"

with app.app_context():
    db.create_all()
    db.session.commit()
