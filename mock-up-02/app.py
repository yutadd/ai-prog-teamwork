from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '1c33c613c2357110a08a8964f4aa621f'  # ここにOpenWeatherMapのAPIキーを入力

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather', methods=['POST'])
def get_weather():
    data = request.json
    city = data.get('city')
    if not city:
        return jsonify({'error': '都市名が指定されていません。'}), 400

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ja'
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        weather = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        return jsonify({'weather': weather, 'temp': temp})
    else:
        return jsonify({'error': '都市が見つかりませんでした。'}), 404

if __name__ == '__main__':
    app.run(debug=True)