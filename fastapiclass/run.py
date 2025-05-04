from src import app

from src.users import user_router
from src.home import home_router

app.include_router(home_router)
app.include_router(user_router)
