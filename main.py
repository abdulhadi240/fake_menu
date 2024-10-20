from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Defining the MenuItem model with an image URL field
class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    price: float
    available: bool
    image_url: str

# Fake menu data with image URLs
menu = [
    {
        "id": 1,
        "name": "Margherita Pizza",
        "description": "Classic pizza with tomato sauce and mozzarella cheese.",
        "price": 8.99,
        "available": True,
        "image_url": "https://cookieandkate.com/images/2021/07/margherita-pizza-recipe-1-2.jpg"
    },
    {
        "id": 2,
        "name": "Pepperoni Pizza",
        "description": "Pizza topped with pepperoni and mozzarella cheese.",
        "price": 9.99,
        "available": True,
        "image_url": "https://i0.wp.com/www.amysrecipebook.com/wp-content/uploads/2021/01/pepperonipizza-8-web.jpg"
    },
    {
        "id": 3,
        "name": "Caesar Salad",
        "description": "Fresh romaine lettuce, croutons, and Caesar dressing.",
        "price": 7.49,
        "available": True,
        "image_url": "https://www.allrecipes.com/thmb/mXZ0Tulwn3x9_YB_ZbkiTveDYFE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/229063-Classic-Restaurant-Caesar-Salad-ddmfs-4x3-231-89bafa5e54dd4a8c933cf2a5f9f12a6f.jpg"
    },
    {
        "id": 4,
        "name": "Spaghetti Carbonara",
        "description": "Pasta with creamy sauce, bacon, and Parmesan cheese.",
        "price": 12.49,
        "available": False,
        "image_url": "https://static01.nyt.com/images/2021/02/14/dining/carbonara-horizontal/carbonara-horizontal-square640-v2.jpg"
    },
    {
        "id": 5,
        "name": "Garlic Bread",
        "description": "Toasted bread with garlic butter.",
        "price": 3.99,
        "available": True,
        "image_url": "https://www.ambitiouskitchen.com/wp-content/uploads/2023/02/Garlic-Bread-4.jpg"
    }
]

# Endpoint to provide all menu items
@app.get("/menu", response_model=List[MenuItem])
def get_menu():
    return menu

