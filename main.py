import requests
import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
import pytz

load_dotenv()

api_key = os.getenv("COINGECKO_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set COINGECKO_API_KEY in your .env file")

def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=crypto-royale&include_24hr_change=true"
    
    headers = {
        "x-cg-demo-api-key": api_key
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def fetch_price():
    price_data = get_crypto_data()
    
    if price_data and "crypto-royale" in price_data:
        asset_data = price_data["crypto-royale"]
        current_price = asset_data.get("usd", "N/A")
        price_change = asset_data.get("usd_24h_change", "N/A")

        print(f"Price: ${current_price} | Change: {price_change}%")
    else:
        print("Failed to fetch price data")

def run_scheduler():
    timezone = pytz.UTC
    
    while True:
        current_time = datetime.now(timezone)
        next_execution = current_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        
        sleep_duration = (next_execution - current_time).total_seconds()
        
        print(f"Next Run: {next_execution.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        time.sleep(sleep_duration)
        fetch_price()

if __name__ == "__main__":
    #fetch_price()
    run_scheduler()
    
