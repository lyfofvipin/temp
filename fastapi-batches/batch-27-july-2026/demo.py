from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/try/query_perm")
def try_query_perm(a, b, c):
    return {
        "A": a,
        "B": b,
        "C": c
    }

@app.get("/try/{dob:path}")
def try_dob(dob):
    return {"DOB": dob}

