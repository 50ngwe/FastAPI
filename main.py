from typing import Optional
from fastapi import FastAPI
import psycopg2
from psycopg2 import Error
import database 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "App"}
    
@app.get("/items/")
def read_item():
    results = database.fetch_all()
    return results

@app.get("/items/{item_id}")
def read_item(item_id: str, q: Optional[str] = None):
    results = database.fetch_one("item_id", item_id)
    return results

@app.post("/item/{item_id}")
def update_item(item_id: str, q: Optional[str] = None):
    results = database.update_one("item_id", item_id)


@app.get("/items/{q_field}/{q_val}")
def read_item(q_field: str, q_val: str):
    results = database.fetch_one(q_field, q_val)
    return results





