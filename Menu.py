from supabase_variables import supabase


def get_menu_items():
    response = supabase.table("menu").select("*").execute()
    return response.data

