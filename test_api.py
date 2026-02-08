"""
Sample test script for the Weather Forecast App API
This demonstrates how to use the API endpoints programmatically
"""

import requests
import json

BASE_URL = 'http://localhost:5000'

def test_weather_api(city):
    """Test the weather API endpoint"""
    print(f"\n{'='*50}")
    print(f"Testing Weather API for: {city}")
    print('='*50)
    
    try:
        response = requests.post(
            f'{BASE_URL}/api/weather',
            json={'city': city},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            
            # Display current weather
            current = data['current']
            print(f"\n📍 Location: {current['city']}, {current['country']}")
            print(f"🌡️  Temperature: {current['temperature']}°C")
            print(f"🤔 Feels like: {current['feels_like']}°C")
            print(f"☁️  Condition: {current['description']}")
            print(f"💧 Humidity: {current['humidity']}%")
            print(f"💨 Wind Speed: {current['wind_speed']} km/h")
            print(f"📊 Pressure: {current['pressure']} hPa")
            
            # Display forecast
            print(f"\n5-Day Forecast:")
            print("-" * 50)
            for day in data['forecast']:
                print(f"{day['date']:15} | {day['temperature']:>5}°C | {day['description']}")
            
            print("\n✅ Test passed!")
            return True
        else:
            print(f"\n❌ Error: {response.json().get('error', 'Unknown error')}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to server. Make sure the app is running!")
        return False
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return False

def test_history_api():
    """Test the history API endpoint"""
    print(f"\n{'='*50}")
    print("Testing History API")
    print('='*50)
    
    try:
        response = requests.get(f'{BASE_URL}/api/history', timeout=10)
        
        if response.status_code == 200:
            history = response.json()
            
            if history:
                print(f"\n📜 Recent Searches ({len(history)} total):")
                print("-" * 50)
                for item in history:
                    print(f"{item['city']:15} | {item['temperature']:>5}°C | {item['description']}")
                print("\n✅ Test passed!")
            else:
                print("\n📝 No search history yet")
                print("✅ Test passed!")
            return True
        else:
            print(f"\n❌ Error: Status code {response.status_code}")
            return False
            
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("\n" + "="*50)
    print("🌤️  Weather Forecast App - API Tests")
    print("="*50)
    
    # Test cities
    test_cities = ['London', 'New York', 'Tokyo', 'Paris']
    
    results = []
    for city in test_cities:
        result = test_weather_api(city)
        results.append(result)
    
    # Test history
    history_result = test_history_api()
    results.append(history_result)
    
    # Summary
    print(f"\n{'='*50}")
    print("Test Summary")
    print('='*50)
    print(f"Total tests: {len(results)}")
    print(f"Passed: {sum(results)}")
    print(f"Failed: {len(results) - sum(results)}")
    
    if all(results):
        print("\n🎉 All tests passed!")
    else:
        print("\n⚠️  Some tests failed. Check the output above.")

if __name__ == '__main__':
    print("\n⚠️  IMPORTANT: Make sure the Flask app is running before running this test!")
    print("Run 'python app.py' in another terminal first.\n")
    
    input("Press Enter to continue with tests...")
    main()
