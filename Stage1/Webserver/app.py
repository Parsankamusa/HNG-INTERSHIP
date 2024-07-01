"""
Provides a simple Flask API endpoint that returns a greeting message with the visitor's IP address, location, and the current temperature in that location.

The `get_location_and_temperature` function is a mock implementation that returns hardcoded data. In a real-world application, this function would make calls to a geolocation and weather API to retrieve the actual location and temperature data.

The `/api/hello` endpoint accepts an optional `visitor_name` query parameter, which is used in the greeting message. If no `visitor_name` is provided, the message will use the default "Visitor".
"""
"""
Provides a simple Flask API endpoint that returns a greeting message with the client's IP address, location, and the current temperature in that location.

The `get_location_and_temperature` function is a mock implementation that returns hardcoded data. In a real-world application, this function would make calls to a geolocation and weather API to retrieve the actual location and temperature data.

The `/api/hello` endpoint accepts an optional `visitor_name` query parameter, which is used in the greeting message. If no `visitor_name` is provided, the message will use the default "Visitor".
"""
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_location_and_temperature(ip):
    # Mock data for demonstration; replace with actual IP geolocation and weather API calls
    return {"city": "Nairobi", "temperature": 20}

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    client_ip = request.remote_addr

    # Get location and temperature for the IP
    location_data = get_location_and_temperature(client_ip)
    city = location_data["city"]
    temperature = location_data["temperature"]

    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
