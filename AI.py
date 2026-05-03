#Collect the information retrieved from the weather API and then use an LLM to interpret it and explain it to the user

from main import info
from openai import OpenAI
import os     
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# This is where we will use the LLM to interpret the data retrieved from the weather API and explain it to the user in a more human-friendly way. We will use the OpenRouter API to access the LLM and generate a response based on the weather data.
def interpret_weather_data(data):
    api_key = os.getenv("OpenRouterKey")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        )
    
    completion = client.chat.completions.create(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that explains weather data to users in a simple and easy-to-understand way."
            },
            {
                "role": "user",
                "content": f"The current weather in {data['city']} is {data['temp_c']}°C with {data['text']}. The maximum temperature for today is {data['maxtemp_c']}°C and the minimum temperature is {data['mintemp_c']}°C. There is a {'chance of rain' if data['will_it_rain'] else 'no chance of rain'} today. Can you explain this weather data to me in a more human-friendly way, please note to not use any emoji and make more of a synopsis than a detailed explanation in each different point?"
            }
        ]
    )
    return completion.choices[0].message.content