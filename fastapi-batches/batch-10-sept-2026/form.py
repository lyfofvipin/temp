from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/")
def home():
    return "This is homepage."

@app.post("/login")
def login( username: str = Form(), password:str = Form() ):
    return "This is the login page."

