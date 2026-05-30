import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COINGECKO_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set COINGECKO_API_KEY in your .env file")

url = "https://api.coingecko.com/api/v3/ping"

headers = {
    "x-cg-demo-api-key": api_key
}

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Success!")
        print(f"Response: {response.json()}")
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
