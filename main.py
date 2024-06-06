from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None


@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: Annotated[int, Body()]):
    # Here, Body() tells that this parameter is Body param
    results = {"item_id": item_id, "item": item, "user": user, "importance":importance}
    return results