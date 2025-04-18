import requests

def fetch_crypto_data():
    # Beispiel: Abrufen von Kryptowährungsdaten
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(api_url)
    return response.json()