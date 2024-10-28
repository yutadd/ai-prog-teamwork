import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherAPI:
    def __init__(self):
        # OpenWeatherMap の無料APIの代わりに wttr.in を使用
        self.base_url = "https://wttr.in"

    def get_weather(self, city):
        try:
            # JSONフォーマットでデータを取得
            response = requests.get(f"{self.base_url}/{city}?format=j1")
            data = response.json()
            
            if response.status_code == 200:
                return {
                    'temperature': data['current_condition'][0]['temp_C'],
                    'weather': data['current_condition'][0]['weatherDesc'][0]['value'],
                    'description': data['current_condition'][0]['weatherDesc'][0]['value'],
                    'humidity': data['current_condition'][0]['humidity']
                }
            else:
                return None
        except:
            return None
