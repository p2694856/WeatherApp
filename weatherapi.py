import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WeatherAPIKey")

def fetch_weather(city):
    # Forecast endpoint is needed for maxtemp and rain chance
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        curr = data['current']
        fore = data['forecast']['forecastday'][0]['day']
        
        return {
            "city": city,
            "temp_c": curr['temp_c'],
            "is_day": curr['is_day'],
            "text": curr['condition']['text'],
            "wind_mph": curr['wind_mph'],
            "uv": curr['uv'],
            "maxtemp_c": fore['maxtemp_c'],
            "mintemp_c": fore['mintemp_c'],
            "will_it_rain": fore['daily_will_it_rain']
        }
    except Exception as e:
        print(f"Error fetching {city}: {e}")
        return None