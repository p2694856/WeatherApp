from weatherapi import fetch_weather, CITIES  # Imports the function and the city list
from input import selectCity  # Import the city selection function
  # Import the function to interpret weather data
def info():
    fetch_weather(selectCity)


if __name__ == "__main__":
    # Collect the city selected by the user
    selectedCity = selectCity()
    print(f"Starting pull for: {selectedCity}...")
    data = fetch_weather(selectedCity)
    from AI import interpret_weather_data

    # If we successfully got data, print the temperature to the console
    if data:
        line = f"City: {data['city']} | Temp: {data['temp_c']}°C | Condition: {data['text']} | Max Temp: {data['maxtemp_c']}°C | Min Temp: {data['mintemp_c']}°C | Chance of Rain: {'Yes' if data['will_it_rain'] else 'No'}\n"
        line2 = interpret_weather_data(data)
        print(line, line2)