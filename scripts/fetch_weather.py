import requests

def fetch_weather_data():
    # Beispiel: Abrufen von Wetterdaten über eine API
    api_url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=your_api_key"
    response = requests.get(api_url)
    return response.json()