import pandas as pd
import requests

# Function to fetch raw data (e.g., from an API or file)
def fetch_raw_data():
    # Example: Fetch weather data from OpenWeatherMap API
    api_key = "your_openweathermap_api_key"
    city = "New York"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Convert JSON data to a DataFrame
    raw_data = pd.DataFrame([data])
    return raw_data

# Function to process raw data
def process_data(raw_data):
    # Example: Extract relevant fields and clean data
    processed_data = raw_data[['name', 'main', 'weather']].copy()

    # Flatten nested JSON fields
    processed_data['temperature'] = processed_data['main'].apply(lambda x: x['temp'])
    processed_data['humidity'] = processed_data['main'].apply(lambda x: x['humidity'])
    processed_data['weather_description'] = processed_data['weather'].apply(lambda x: x[0]['description'])

    # Drop unnecessary columns
    processed_data.drop(columns=['main', 'weather'], inplace=True)

    return processed_data.to_dict(orient='records')