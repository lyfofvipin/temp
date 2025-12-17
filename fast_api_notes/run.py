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
