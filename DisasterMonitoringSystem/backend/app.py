from flask import Flask, jsonify, request
import data_processing as dp

app = Flask(__name__)

# Route to fetch processed data
@app.route('/api/odisha/weather', methods=['GET'])
def get_odisha_weather():
    weather_data = dp.fetch_odisha_weather()
    processed_data = dp.process_data(weather_data)
    return jsonify(processed_data)

@app.route('/api/odisha/flood', methods=['GET'])
def get_odisha_flood_data():
    flood_data = dp.fetch_odisha_flood_data()
    return jsonify(flood_data.to_dict(orient='records'))

@app.route('/api/odisha/cyclone', methods=['GET'])
def get_odisha_cyclone_data():
    cyclone_data = dp.fetch_odisha_cyclone_data()
    return jsonify(cyclone_data.to_dict(orient='records'))

# Route to send alerts
@app.route('/api/alert', methods=['POST'])
def send_alert():
    data = request.json  # Get alert data from the request
    # Add logic to send alerts (e.g., via SMS, email, or push notifications)
    return jsonify({"status": "Alert sent!", "data": data})

def send_odisha_alert(message):
    telegram_bot_token = "your_telegram_bot_token"
    chat_id = "odisha_disaster_chat_id"
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    requests.get(url, params=params)

if __name__ == '__main__':
    app.run(debug=True)
    
# Note: Geetika has joined, ab ye project ho jaega complete.