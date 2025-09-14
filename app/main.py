# FastAPI demo app
from fastapi import FastAPI

app = FastAPI(title="Generic FastAPI App")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
def health():
    return {"status": "ok"}
