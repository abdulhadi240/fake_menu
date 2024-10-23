from supabase_variables import supabase


def get_order():
    response = supabase.table("orders").select("*").execute()
    return response.data

