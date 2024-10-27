from supabase_variables import supabase
from order_email import create_order_template

def get_order():
    response = supabase.table("orders").select("*").execute()
    return response.data


def create_orders(email, menuid, quantity, address , instruction, status, date):
    
    customer_response = (
        supabase.table("customers")
        .select("*")
        .eq("email", email)
        .execute()
    )

    if not customer_response.data:
        return "Customer not found plz create a new customer"

    # Extract customerid from the response
    customerid = customer_response.data[0]["customerid"]
    customer_name = customer_response.data[0]["firstname"] + " " + customer_response.data[0]["lastname"]
    phone_number = customer_response.data[0]["phonenumber"]
    
    
    response = (
        supabase.table("orders")
        .insert({
            "customerid": customerid, 
            "menuid": menuid, 
            "quantity": quantity, 
            "status": status, 
            "orderdate": date,
            "address": address,
            "Instruction": instruction
        })
        .execute()
    )
    if response.data:
        create_order_template(customerid, customer_name, email, phone_number, menuid, quantity, instruction)
        return "Success"
    else :
        return "Unsuccessful"
