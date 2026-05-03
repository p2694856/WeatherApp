# WeatherApp

A Python-based application that scrapes weather information from [WeatherAPI](https://weatherapi.com/) and provides human-friendly summaries using an AI Large Language Model (LLM).

## Overview

The WeatherApp allows users to select one of five major UK cities and retrieve real-time weather data. Beyond just showing raw numbers, the app integrates with an AI assistant to interpret the data (temperature, rain probability, conditions) and present it as a concise, readable synopsis.

### Key Features
* **Real-time Data**: Fetches current temperature, conditions, and daily forecast extremes (max/min) from WeatherAPI.
* **AI Interpretation**: Uses an LLM (via OpenRouter) to translate technical weather data into a "human-friendly" summary.
* **Input Validation**: A robust input loop ensures users select from the supported cities: London, Edinburgh, Cardiff, Belfast, or Birmingham. 
* **Testing Suite**: Includes logic to batch-pull data for multiple cities and export results to text files for verification.

## How It Works

1.  **Selection**: The user is prompted to input a city name. [cite: 4]
2.  **API Pull**: The `weatherapi.py` script makes a request to the WeatherAPI forecast endpoint using a secure API key.
3.  **Processing**: The application extracts key metrics like current temperature, UV index, and chance of rain.
4.  **AI Summary**: The raw data is sent to an LLM (Nvidia Nemotron model) to generate a brief weather synopsis.

## Future Plans

The current version of this project serves as the backend logic and proof of concept. The next steps for development include:
* **Web Integration**: Moving the Python logic into a web framework (such as Flask or Django) to create a fully functional website.
* **Frontend UI**: Developing a clean, responsive user interface to display weather summaries and icons.
* **Expanded City Support**: Allowing users to search for any global city rather than a pre-defined list.
* **Enhanced AI Features**: Adding personalized clothing recommendations or activity suggestions based on the AI's weather interpretation.

## Setup

The project requires a `.env` file containing the following keys:
* `WeatherAPIKey`: Your API key from weatherapi.com.
* `OpenRouterKey`: Your API key for LLM access via OpenRouter.
