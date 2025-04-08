from src import app, db

class User( db.Model ):

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String )
    email = db.Column( db.String )
    password = db.Column( db.String )

with app.app_context():
    db.create_all()
    db.session.commit()
