from supabase_variables import supabase
from email_complaint import send_complaint_email


def create_complaint(firstname, email, text, date):
    # Query to find the customer by firstname and email
    customer_response = (
        supabase.table("customers")
        .select("*")
        .eq("firstname", firstname)
        .eq("email", email)
        .execute()
    )

    if not customer_response.data:
        return "Customer not found. Please check the details."

    # Extract customerid from the response
    customerid = customer_response.data[0]["customerid"]
    phonenumber = customer_response.data[0]["phonenumber"]

    # Set complaint status
    status = 'Pending'

    # Insert the complaint
    complaint_response = (
        supabase.table("complaints")
        .insert({
            "customerid": customerid,
            "complainttext": text,
            "complaintdate": date,
            "status": status
        })
        .execute()
    )
    
    send_complaint_email(customerid, firstname , email, phonenumber, text)

    if complaint_response.data:
        return "Successfully created your complaint and passed to relevant department."
    else:
        return "Failed to create the complaint."



print(create_complaint("Hadi","ah91@gmail.com","12/12/12","the food is very bad"))