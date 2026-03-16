from src import users, models, auth, tasks
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.user_routes)
app.include_router(auth.login_logout)
app.include_router(tasks.task_route)
