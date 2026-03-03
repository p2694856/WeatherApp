from weatherapi import fetch_weather, CITIES  # Imports the function and the city list

def test_pull_logic():
    # We only want the first two cities from your CITIES list
    test_cities = CITIES[:2] 
    results = []

    print(f"Starting test pull for: {test_cities}...")

    for city in test_cities:
        data = fetch_weather(city)
        if data:
            results.append(data)

    # If we successfully got data, write the temperatures to a file
    if len(results) >= 2:
        with open('test_output.txt', 'w') as f:
            for entry in results:
                line = f"City: {entry['city']} | Temp: {entry['temp_c']}°C\n"
                f.write(line)
        print("Test successful! Check 'test_output.txt' for the results.")
    else:
        print("Test failed: Could not extract data for at least two cities.")

# This line ensures the test only runs if you run output.py directly
if __name__ == "__main__":
    print("--- DEBUG: Script Started ---")
    test_pull_logic()