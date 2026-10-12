import os
from dotenv import load_dotenv,dotenv_values,find_dotenv

# Load .env file from the current directory
load_dotenv(find_dotenv())
config = dotenv_values(find_dotenv())
api_key = config.get("API_KEY")
api_secret = os.get("API_SECRET","")
api_key = os.environ("API_KEY")