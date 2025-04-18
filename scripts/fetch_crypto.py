import requests
import os

def fetch_crypto_data():
    # Fetch the API key from environment variables, defaulting to a placeholder if not found
    api_key = os.getenv('CRYPTO_API_KEY', 'your_default_api_key')
    
    # Construct the API URL for fetching cryptocurrency prices
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    
    try:
        # Make the request to the CoinGecko API
        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful
        return response.json()  # Return the response as JSON
    except requests.exceptions.RequestException as e:
        # Handle any exceptions during the API request
        print(f"Error fetching crypto data: {e}")
        return None