# Weather Forecast App

A modern, feature-rich weather forecast application built with Python Flask, REST APIs, and SQLite. Get real-time weather data and 5-day forecasts for any city worldwide.

## Features

- **Real-time Weather Data**: Get current weather conditions for any city
- **5-Day Forecast**: View upcoming weather predictions
- **Search History**: Track your recent weather searches stored in SQLite database
- **Beautiful UI**: Modern, responsive design that works on all devices
- **REST API Integration**: Fetches data from OpenWeatherMap API
- **JSON Data Processing**: Handles and parses weather data efficiently
- **SQLite Database**: Stores search history for easy reference

## Technologies Used

- **Backend**: Python, Flask
- **API**: OpenWeatherMap REST API
- **Database**: SQLite3
- **Data Format**: JSON
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **HTTP Requests**: Python Requests library

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- OpenWeatherMap API key (free tier available)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/weather-forecast-app.git
   cd weather-forecast-app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your API key**
   - Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/api)
   - Generate an API key from your account dashboard

5. **Configure the API key**
   
   You have two options:
   
   **Option 1: Environment Variable (Recommended)**
   ```bash
   # On Windows
   set OPENWEATHER_API_KEY=your_api_key_here
   
   # On macOS/Linux
   export OPENWEATHER_API_KEY=your_api_key_here
   ```
   
   **Option 2: Direct in Code**
   - Open `app.py`
   - Replace `'your_api_key_here'` with your actual API key on line 10

## Usage

1. **Run the application**
   ```bash
   python app.py
   ```

2. **Access the app**
   - Open your web browser
   - Navigate to `http://localhost:5000`

3. **Search for weather**
   - Enter any city name in the search box
   - Click "Search" to view current weather and 5-day forecast
   - Check the "Recent Searches" section to see your search history

## Project Structure

```
weather-forecast-app/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── weather.db             # SQLite database (auto-created)
├── README.md              # Project documentation
│
├── templates/
│   └── index.html         # Frontend HTML template
│
└── .gitignore            # Git ignore file
```

## API Endpoints

### Get Weather Data
- **URL**: `/api/weather`
- **Method**: `POST`
- **Body**: `{"city": "London"}`
- **Response**: JSON with current weather and 5-day forecast

### Get Search History
- **URL**: `/api/history`
- **Method**: `GET`
- **Response**: JSON array of recent searches

## Database Schema

```sql
CREATE TABLE weather_history (
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
);
```

## Features Breakdown

### Current Weather Display
- Temperature (Celsius)
- Feels like temperature
- Weather description and icon
- Humidity percentage
- Wind speed (km/h)
- Atmospheric pressure

### 5-Day Forecast
- Daily temperature predictions
- Weather conditions
- Visual weather icons
- Date display

### Search History
- Automatically saves all searches
- Displays last 10 searches
- Shows temperature and conditions
- Timestamp for each search

## Customization

You can customize the app by:
- Changing the color scheme in `templates/index.html` (CSS section)
- Modifying temperature units (change `units='metric'` to `units='imperial'` in `app.py`)
- Adjusting forecast days displayed
- Adding more weather parameters

## Troubleshooting

**Problem**: API key error
- **Solution**: Make sure you've activated your API key on OpenWeatherMap (can take a few minutes)

**Problem**: City not found
- **Solution**: Try using the full city name or add country code (e.g., "London,UK")

**Problem**: Database error
- **Solution**: Delete `weather.db` and restart the app to recreate the database
