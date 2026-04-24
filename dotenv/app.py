import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("API_KEY")
app_name = os.environ.get("APP_NAME")
print(f"Starting {app_name}...")
if api_key:
    print(f"API key loaded successfully: {api_key[:4]}...")
else:
    print("ERROR: API_KEY not found. Did you create a .env file?")
    