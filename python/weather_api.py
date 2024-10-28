import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherAPI:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ja'
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                return {
                    'temperature': data['main']['temp'],
                    'weather': data['weather'][0]['main'],
                    'description': data['weather'][0]['description'],
                    'humidity': data['main']['humidity']
                }
            else:
                return None
        except:
            return None

print("test")
