from supabase_variables import supabase


def create_customer(firstname, lastname, email, phonenumber, date):
    response = (
        supabase.table("customers")
        .insert({
            "firstname": firstname, 
            "lastname": lastname, 
            "email": email, 
            "phonenumber": phonenumber, 
            "datejoined": date
        })
        .execute()
    )
    if response.data:
        return "Success"
    else :
        return "Unsuccessful"
    
    
    
    
