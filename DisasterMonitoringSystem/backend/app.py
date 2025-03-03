from flask import Flask, jsonify, request
import data_processing as dp

app = Flask(__name__)

# Route to fetch processed data
@app.route('/api/data', methods=['GET'])
def get_data():
    # Fetch raw data (e.g., from an API or file)
    raw_data = dp.fetch_raw_data()

    # Process the data
    processed_data = dp.process_data(raw_data)

    # Return processed data as JSON
    return jsonify(processed_data)

# Route to send alerts
@app.route('/api/alert', methods=['POST'])
def send_alert():
    data = request.json  # Get alert data from the request
    # Add logic to send alerts (e.g., via SMS, email, or push notifications)
    return jsonify({"status": "Alert sent!", "data": data})

if __name__ == '__main__':
    app.run(debug=True)