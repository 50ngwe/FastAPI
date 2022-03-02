from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{Color}")
def read_item(Color: string, Available: Optional[str] = None):
    return {"Car Color": item_id, "Available": q}

