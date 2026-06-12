from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI(title="FastAPI — Assignment Demo")

class Item(BaseModel):
    id: str | None = None
    name: str
    description: str | None = None
    done: bool = False

items: List[Item] = []

@app.get("/items", response_model=List[Item])
def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    item.id = str(uuid4())
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, updated: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            updated.id = item_id
            items[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: str):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return
    raise HTTPException(status_code=404, detail="Item not found")
