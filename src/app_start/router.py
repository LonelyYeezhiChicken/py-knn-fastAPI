from fastapi import FastAPI
from src.controller.homeController import read_root, read_item, update_item

app = FastAPI()

app.get("/")(read_root)
app.get("/items/{item_id}")(read_item)
app.put("/items/{item_id}")(update_item)
