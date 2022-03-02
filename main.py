from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{Color}")
def read_item(Pick_Color: str, Available: Optional[str] = None):
    return {"Car Color": Pick_Color, "Available": q}

