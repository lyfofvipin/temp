from fastapi import FastAPI, status, Response

app = FastAPI()

@app.get("/test")
def test(res : Response):
    res.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "hello"}

@app.get("/demo", status_code=status.HTTP_100_CONTINUE)
def test():
    return {"message": "hello"}

