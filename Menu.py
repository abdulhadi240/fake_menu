import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

# Ensure the environment variables are not None
if url is None or key is None:
    raise ValueError("Supabase URL and Key must be set as environment variables.")

supabase: Client = create_client(url, key)
def get_menu_items():
    response = supabase.table("menu").select("*").execute()
    return response.data

