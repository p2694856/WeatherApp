import requests
import os
from dotenv import load_dotenv

CITIES = ["London", "Cardiff", "Belfast", "Edinburgh", "Birmingham"]
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
    
# --- This part tells Python to actually RUN the code ---
if __name__ == "__main__":
    # Your city list
    CITIES = ["London", "Cardiff", "Belfast", "Edinburgh", "Birmingham"]
    
    print("Starting test pull...")
    
    # We only want the first two cities for this check
    for city in CITIES[:2]:
        print(f"Checking {city}...")
        result = fetch_weather(city)
        
        if result:
            # Output the temperature for the city to a file
            with open("test_output.txt", "a") as f:
                f.write(f"City: {result['city']} | Temp: {result['temp_c']}°C\n")
            print(f"Done: {result['city']} saved.")
        else:
            print(f"Failed to get data for {city}.")

    print("Check finished. Look for test_output.txt in your folder.")