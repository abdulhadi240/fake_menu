from supabase_variables import supabase


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
    
    
    response = (
        supabase.table("orders")
        .insert({
            "customerid": customerid, 
            "menuid": menuid, 
            "quantity": quantity, 
            "status": status, 
            "orderdate": date,
            "address": address,
            "instruction": instruction
        })
        .execute()
    )
    if response.data:
        return "Success"
    else :
        return "Unsuccessful"
