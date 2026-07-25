from run import app
from src import SQLAlchemy, UserMixin

db = SQLAlchemy( app )

class Users( db.Model, UserMixin ):

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String, nullable = False  )
    email = db.Column( db.String, nullable = False, unique = True )
    password = db.Column( db.String, nullable = False  )
    collage = db.Column( db.String )
    photo = db.Column( db.String )

    posts = db.relationship("Post")

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    user_id = db.Column( db.Integer, db.ForeignKey('users.id'), nullable=False )


with app.app_context():
    db.create_all()
