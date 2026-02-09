from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def test():
    return {}

@app.get("/users")
def user():
    with open("dummy_user_data.json") as f:
        data = json.load(f)

    final_data = []
    data = data["users"]
    for x in data:
        final_data.append(x.get("firstName"))
    return final_data

