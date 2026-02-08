from flask import Flask, render_template, request, jsonify
import requests
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# OpenWeatherMap API configuration
API_KEY = os.environ.get('OPENWEATHER_API_KEY', 'your_api_key_here')
BASE_URL = 'https://api.openweathermap.org/data/2.5'

# Database setup
def init_db():
    """Initialize the SQLite database"""
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            country TEXT,
            temperature REAL,
            feels_like REAL,
            humidity INTEGER,
            pressure INTEGER,
            weather_description TEXT,
            wind_speed REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(weather_data):
    """Save weather data to database"""
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather_history 
        (city, country, temperature, feels_like, humidity, pressure, 
         weather_description, wind_speed)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        weather_data['city'],
        weather_data['country'],
        weather_data['temperature'],
        weather_data['feels_like'],
        weather_data['humidity'],
        weather_data['pressure'],
        weather_data['description'],
        weather_data['wind_speed']
    ))
    conn.commit()
    conn.close()

def get_weather(city):
    """Fetch current weather data from OpenWeatherMap API"""
    try:
        url = f"{BASE_URL}/weather"
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp'], 1),
            'feels_like': round(data['main']['feels_like'], 1),
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'].title(),
            'icon': data['weather'][0]['icon'],
            'wind_speed': round(data['wind']['speed'] * 3.6, 1)  # Convert m/s to km/h
        }
        
        # Save to database
        save_to_db(weather_data)
        
        return weather_data, None
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching weather data: {str(e)}"
    except KeyError as e:
        return None, f"City not found or invalid response"

def get_forecast(city):
    """Fetch 5-day weather forecast from OpenWeatherMap API"""
    try:
        url = f"{BASE_URL}/forecast"
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Process forecast data - get one forecast per day at noon
        forecast_list = []
        seen_dates = set()
        
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt']).date()
            hour = datetime.fromtimestamp(item['dt']).hour
            
            # Get forecast around noon (12:00) for each day
            if date not in seen_dates and 11 <= hour <= 13:
                forecast_list.append({
                    'date': date.strftime('%a, %b %d'),
                    'temperature': round(item['main']['temp'], 1),
                    'description': item['weather'][0]['description'].title(),
                    'icon': item['weather'][0]['icon'],
                    'humidity': item['main']['humidity']
                })
                seen_dates.add(date)
                
                if len(forecast_list) >= 5:
                    break
        
        return forecast_list, None
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching forecast: {str(e)}"
    except KeyError:
        return None, "City not found or invalid response"

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/weather', methods=['POST'])
def api_weather():
    """API endpoint to get weather data"""
    city = request.json.get('city', '').strip()
    
    if not city:
        return jsonify({'error': 'City name is required'}), 400
    
    weather_data, error = get_weather(city)
    
    if error:
        return jsonify({'error': error}), 404
    
    forecast_data, forecast_error = get_forecast(city)
    
    return jsonify({
        'current': weather_data,
        'forecast': forecast_data if not forecast_error else []
    })

@app.route('/api/history')
def api_history():
    """API endpoint to get weather search history"""
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT city, country, temperature, weather_description, timestamp 
        FROM weather_history 
        ORDER BY timestamp DESC 
        LIMIT 10
    ''')
    rows = cursor.fetchall()
    conn.close()
    
    history = [{
        'city': row[0],
        'country': row[1],
        'temperature': row[2],
        'description': row[3],
        'timestamp': row[4]
    } for row in rows]
    
    return jsonify(history)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
