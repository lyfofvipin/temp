from src import app
from src import views
from src.auth import lm

lm.init_app(app)
app.run()
