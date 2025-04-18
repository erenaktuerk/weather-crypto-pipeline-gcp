import streamlit as st
import requests
import os

# Fetch weather data using OpenWeatherMap API
def fetch_weather_data():
    api_key = os.getenv('WEATHER_API_KEY', 'your_default_api_key')
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"
    response = requests.get(api_url)
    return response.json() if response.status_code == 200 else None

# Fetch cryptocurrency data using CoinGecko API
def fetch_crypto_data():
    api_key = os.getenv('CRYPTO_API_KEY', 'your_default_api_key')
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(api_url)
    return response.json() if response.status_code == 200 else None

# Define the Streamlit app layout and functionality
def app():
    st.title('Weather and Crypto Dashboard')
    
    # Display weather data
    st.header('Weather Data')
    weather_data = fetch_weather_data()
    if weather_data:
        st.write(f"Temperature: {weather_data['main']['temp']} °C")
        st.write(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        st.write("Could not fetch weather data.")

    # Display cryptocurrency data
    st.header('Crypto Data')
    crypto_data = fetch_crypto_data()
    if crypto_data:
        st.write(f"Bitcoin: ${crypto_data['bitcoin']['usd']}")
        st.write(f"Ethereum: ${crypto_data['ethereum']['usd']}")
    else:
        st.write("Could not fetch crypto data.")

# Run the app
if __name__ == '__main__':
    app()