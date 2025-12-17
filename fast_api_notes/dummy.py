from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json


app = FastAPI()

# Add CORS middleware to allow requests from HTML file
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. For production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

with open("python_qna.json") as file_obj:
    data = json.load(file_obj)
    data = data["questions"]


@app.get("/all_qn")
def all_qn():
    data_to_return = []
    for x in data:
        data_to_return.append({
            "question": x.get("question"),
            "id": x.get("id")
        })
    return data_to_return

@app.get("/options/{id}")
def get_options(id: int):

    for x in data:
        if x.get("id") == id:
            return x.get("options")

@app.get("/check_ans/{id}/{ans}")
def check_ans( id:int, ans ):

    for x in data:
        if x.get("id") == id:
            if ans == x.get("answer"):
                return True
            else:
                return False
    return {
        "message": "ID not found"
    }
