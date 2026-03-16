from . import app, login_manager, UserMixin
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy
database = SQLAlchemy(app)
migrate = Migrate(app, database)


class User(database.Model, UserMixin):

    id = database.Column( database.Integer, primary_key = True )
    username = database.Column( database.String(10), unique=True, nullable=False )
    email = database.Column( database.String(100), unique=True, nullable=False )
    password = database.Column( database.String(30), nullable=False )
    name = database.Column( database.String(200) )
    mob = database.Column( database.String(10) )
    is_active = database.Column( database.Boolean, default=True )
    profile_photo = database.Column( database.String(200), default = "static/profile_pics/dafault.png" )

    def __repr__(self):
        return f"<{self.id}, {self.name}, {self.username}>"

with app.app_context():
    database.create_all()

@login_manager.user_loader
def get_user(id):
    return User.query.get(int(id))
