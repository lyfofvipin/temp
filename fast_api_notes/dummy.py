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

from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def test():
    return {"title": "Home Page"}

@app.get("/about")
def test():
    return {"title": "About Page"}

@app.get( "/username/{b}" )
def dynam( b:str ):
    return { "type": b }

@app.get( "/test" )
def dynam( a = 10, b = "23", c= True ):
    return { 
        "b": [a, b, c]
    }

@app.get( "/test/{b}/{c}/{d}" )
def dynam( b, c, d ):
    return { "type": [b, c , d] }

@app.get( "/check_eligibility" )
def register( name:str, age:int ):
    if age >= 18:
        return {
            "message": f"Yes {name}, You can Vote.",
            "status": True
        }
    else:
        return {
            "message": f"No {name}, You can not Vote come after {18-age} years.",
            "status": False
        }


from fastapi import FastAPI, status, Response
import json

app = FastAPI()

@app.post("/create")
def create_task( task_title:str, response: Response , completed: bool = False):

    with open("todo_app_database.json") as f:
        existing_data = json.load(f)
    
    data_dict = {
        "title": task_title,
        "completed": completed
    }

    for x in existing_data:
        if task_title == x.get("title"):
            response.status_code = status.HTTP_406_NOT_ACCEPTABLE
            return {"message": "A title with this name is already existed."}

    existing_data.append(data_dict)

    with open("todo_app_database.json", "w") as f:
        json.dump(existing_data, f)

    response.status_code = status.HTTP_201_CREATED
    return {"message": "Task added to the TO-DO list."}

@app.put("/update")
def update_task( completed:bool, response: Response, title:str = "" ):

    with open("todo_app_database.json") as f:
        existing_data = json.load(f)
    
    for x in existing_data:
        if title == x.get("title"):
            x["completed"] = completed
            with open("todo_app_database.json", "w") as f:
                json.dump(existing_data, f)
            return { "message": f"{title} is marked as {completed}." }
    

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "Title Not found."}

@app.get("/read")
def read_data():

    with open("todo_app_database.json") as f:
        existing_data = json.load(f)

    return existing_data

@app.delete("/delete")
def delete(response: Response, title:str = ""):
    
    with open("todo_app_database.json") as f:
        existing_data = json.load(f)
    
    for x in existing_data:
        if title == x.get("title"):
            existing_data.remove(x)
            with open("todo_app_database.json", "w") as f:
                json.dump(existing_data, f)
            return { "message": "data deleted"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "Title Not found."}

from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class Transport(BaseModel):
    dr_name: str
    tr_description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.get("/test/{data}")
def create_item(data):
    return data

@app.get("/test_qp/")
def create_item(data):
    return data

@app.post("/items/")
def create_item(item: Item, tf: Transport):
    return [item, tf]

from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    roll_number: str
    stream: str
    mob: str
    password: str

class Takeinput(BaseModel):
    name: str
    age: int

@app.post("/login/")
async def login(data: Annotated[ Student, Form() ]):
    return data

@app.post("/test/")
async def login(a, b):
    return a

@app.post("/check_eligibility_post/")
def test(data: Annotated[ Takeinput, Form() ]):
    return data.age


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AgeVal(BaseModel):
    name: str
    age: int


@app.get( "/check_eligibility" )
def register( name:str, age:int ):
    if age >= 18:
        return {
            "message": f"Yes {name}, You can Vote.",
            "status": True
        }
    else:
        return {
            "message": f"No {name}, You can not Vote come after {18-age} years.",
            "status": False
        }

@app.post( "/check_eligibility_post" )
def register( name:str, age:int ):
    if age >= 18:
        return {
            "message": f"Yes {name}, You can Vote.",
            "status": True
        }
    else:
        return {
            "message": f"No {name}, You can not Vote come after {18-age} years.",
            "status": False
        }



from fastapi import FastAPI, status, Response, Form
from typing import Annotated
from pydantic import BaseModel
import json
import pdb

app = FastAPI()

class Login(BaseModel):
    username: str
    passwd: str

@app.post("/login")
def login(login_info: Annotated[Login, Form()]):
    if login_info.username == "admin" and login_info.passwd == "123":
        return {"message": "login done."}
    return {"message": "Invalid username or password."}

@app.post("/create")
def create_task( task_title:str, response: Response , login_data: Annotated[Login, Form()] , completed: bool = False):
    login_return_info = login(login_data)
    if "Invalid" in login_return_info.get("message"):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return login_return_info

    with open("todo_app_database.json") as f:
        existing_data = json.load(f)
    
    data_dict = {
        "title": task_title,
        "completed": completed
    }

    for x in existing_data:
        if task_title == x.get("title"):
            response.status_code = status.HTTP_406_NOT_ACCEPTABLE
            return {"message": "A title with this name is already existed."}

    existing_data.append(data_dict)

    with open("todo_app_database.json", "w") as f:
        json.dump(existing_data, f)

    response.status_code = status.HTTP_201_CREATED
    return {"message": "Task added to the TO-DO list."}

@app.put("/update")
def update_task( completed:bool, response: Response, login_data = Annotated[Login, Form()], title:str = "" ):
    login_return_info = login(login_data)
    if "Invalid" in login_return_info.get("message"):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return login_return_info
    with open("todo_app_database.json") as f:
        existing_data = json.load(f)
    
    for x in existing_data:
        if title == x.get("title"):
            x["completed"] = completed
            with open("todo_app_database.json", "w") as f:
                json.dump(existing_data, f)
            return { "message": f"{title} is marked as {completed}." }
    

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "Title Not found."}

@app.get("/read")
def read_data(response: Response, login_data = Annotated[Login, Form()]):
    login_return_info = login(login_data)
    if "Invalid" in login_return_info.get("message"):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return login_return_info
    
    with open("todo_app_database.json") as f:
        existing_data = json.load(f)

    return existing_data

@app.delete("/delete")
def delete(response: Response, login_data = Annotated[Login, Form()], title:str = ""):
    login_return_info = login(login_data)
    if "Invalid" in login_return_info.get("message"):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return login_return_info
    with open("todo_app_database.json") as f:
        existing_data = json.load(f)
    
    for x in existing_data:
        if title == x.get("title"):
            existing_data.remove(x)
            with open("todo_app_database.json", "w") as f:
                json.dump(existing_data, f)
            return { "message": "data deleted"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "Title Not found."}
