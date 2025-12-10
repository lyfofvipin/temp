from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def test():
    return {"title": "Home Page"}

@app.get("/show_name")
def user():
    with open("data_output.json") as f:
        return json.load(f)

@app.get("/firstname")
def fist_name():
    with open("dummy_user_data.json") as file:
        data = json.load(file)
    
    data_to_return = []
    for x in data.get("users"):
        data_to_return.append(x.get("firstName"))

    return data_to_return


@app.get("/name_mail")
def fist_name():
    with open("dummy_user_data.json") as file:
        data = json.load(file)
    
    data_to_return = []
    for x in data.get("users"):
        data_to_return.append(
            {
                "name": x.get("firstName"),
                "mail": x.get("email")
            }
        )

    return data_to_return

