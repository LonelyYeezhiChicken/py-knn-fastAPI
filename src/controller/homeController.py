from typing import Union
from src.model.ItemDto import Item


async def read_root():
    return {"Hello": "World"}


async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
