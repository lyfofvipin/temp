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

with app.app_context():
    db.create_all()
