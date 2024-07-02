
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


def get_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        city = data.get('city')
        region = data.get('regionName')
        country = data.get('country')
        return city, region, country
    except Exception as e:
        print(f"Error fetching location: {e}")
        return None, None, None

def get_temperature(city):
    try:
        api_key = "OPENWEATHERMAP_API_KEY"
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")
        data = response.json()
        return data['main']['temp']
    except:
        return None

def get_location_and_temperature(ip):
    return {"city": "Nairobi", "temperature": 20}

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    
    client_ip = "8.8.8.8"  

    city, region, country = get_location(client_ip)
    if city is None:
        city = "Unknown"
    
    temperature = get_temperature(city)
    if temperature is None:
        temperature = "Unknown"

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {city}"

    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
