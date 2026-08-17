from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/login")
def login(username: str, password: str):
    if username == 'admin' and password == "123":
        return {
            "status": True,
            "message": "Login Done"
        }
    else:
        return {
            "status": False,
            "message": "Invalid Login Details."
        }


@app.post("/login_post")
def login_post(username: str = Form(), password: str = Form()):
    if username == 'admin' and password == "123":
        return {
            "status": True,
            "message": "Login Done"
        }
    else:
        return {
            "status": False,
            "message": "Invalid Login Details."
        }

@app.post("/method3")
def login_post(data: dict):
    return {
        "status": True,
        "data": data,
        "message": "API worked."
    }

