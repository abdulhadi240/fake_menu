from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from classes import Customers_class
from Menu import get_menu_items
from Customers import create_customer
from orders import get_order
from classes import Complain_Classes
from complain import create_complaint
app = FastAPI()


# Endpoint to provide all menu items
@app.get("/menu")
def get_menu():
    response = get_menu_items()
    return response




@app.get("/get_orders")
def get_order_details():
    response = get_order()
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


@app.post("/create_complain")
def generate_new_complain(complain: Complain_Classes):
    response = create_complaint(
        complain.firstname,
        complain.email,
        complain.complain,
        complain.date
    )
    return response 

