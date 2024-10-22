from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from Menu import get_menu_items

app = FastAPI()


# Endpoint to provide all menu items
@app.get("/menu")
def get_menu():
    response = get_menu_items()
    return response



