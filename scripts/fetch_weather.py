import requests
import os

def fetch_weather_data():
    # Fetch the API key from environment variables, defaulting to a placeholder if not found
    api_key = os.getenv('WEATHER_API_KEY', 'your_default_api_key')
    
    # Construct the API URL using the city and the API key
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"
    
    try:
        # Make the request to the OpenWeatherMap API
        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful
        return response.json()  # Return the response as JSON
    except requests.exceptions.RequestException as e:
        # Handle any exceptions during the API request
        print(f"Error fetching weather data: {e}")
        return None