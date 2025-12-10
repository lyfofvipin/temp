from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/about")
def about():
    return { "data": "about"  }

@app.get( "/list/{data}" )
def home_func( data ):
    return { "mid route": data }

@app.get( "/{data}" )
def home_func( data ):
    return { "value": data }
