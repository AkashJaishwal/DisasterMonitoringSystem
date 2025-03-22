import pandas as pd
import requests

# Function to fetch weather data (e.g., from an API or file)
def fetch_odisha_weather():
    # Example: Fetch weather data from OpenWeatherMap API
    api_key = "28c268f0c635a0e2371468cef6049e52"
    city = "Bhubaneswar"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame([data])

def fetch_odisha_flood_data():
    # Example: Fetch flood data from CWC (pseudo-code)
    cwc_url = "https://cwc.gov.in/flood-forecast"
    # Use web scraping or APIs to fetch data
    flood_data = pd.read_csv('data/odisha_flood_data.csv')  # Example
    return flood_data

def fetch_odisha_cyclone_data():
    # Example: Fetch cyclone data from IMD (pseudo-code)
    imd_url = "https://mausam.imd.gov.in/cyclone"
    # Use web scraping or APIs to fetch data
    cyclone_data = pd.read_csv('data/odisha_cyclone_data.csv')  # Example
    return cyclone_data

def send_odisha_alert(message):
    telegram_bot_token = "your_telegram_bot_token"
    chat_id = "odisha_disaster_chat_id"
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    requests.get(url, params=params)

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