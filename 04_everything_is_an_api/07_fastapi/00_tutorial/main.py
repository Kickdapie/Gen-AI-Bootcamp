from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Enum for item categories
class Category(Enum):
    TOOLS = 'tools'
    CONSUMABLES = 'consumables'

# Pydantic model for items
class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category

# In-memory data store
items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=1.99, count=100, id=2, category=Category.CONSUMABLES),
}

# Root route to show all items
@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}

# Query item by ID
@app.get("/items/{item_id}")
def query_item_by_id(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} does not exist.")
    return items[item_id]

# Query item by optional parameters
@app.get("/items/")
def query_item_by_parameters(
    name: str | None = None, 
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,  
):
    def check_items(item: Item) -> bool:
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count == count,
                category is None or item.category is category,
            )
        )
    selection = [item for item in items.values() if check_items(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }

# Add a new item
@app.post("/")
def add_item(item: Item) -> dict[str, Item]:
    if item.id in items:
        raise HTTPException(status_code=400, detail=f"Item with id={item.id} already exists.")
    items[item.id] = item
    return {"added": item}

# Update an existing item
@app.put("/items/{item_id}")
def update_item(
    item_id: int, 
    name: str | None = None,
    price: float | None = None,
    count: int | None = None, 
) -> dict[str, Item]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} does not exist.")
    
    item = items[item_id]

    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count

    return {"updated": item}

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} does not exist.")
    item = items.pop(item_id)
    return {"deleted": item}