from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from classes import Customers_class
from Menu import get_menu_items
from Customers import create_customer, get_costumers
app = FastAPI()


# Endpoint to provide all menu items
@app.get("/menu")
def get_menu():
    response = get_menu_items()
    return response

# Endpoint to provide all menu items
@app.get("/get_costumers")
def get_costumers_info():
    response = get_costumers()
    return response


@app.post("/create_costumers")
def create_costumers_info(customers: Customers_class):
    response = create_customer(
        customers.firstname,
        customers.lastname,
        customers.email,
        customers.phonenumber,
        customers.date
    )
    return response

