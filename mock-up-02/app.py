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
        advice = get_clothing_advice(temp)
        return jsonify({'weather': weather, 'temp': temp, 'advice': advice})
    else:
        return jsonify({'error': '都市が見つかりませんでした。'}), 404

def get_clothing_advice(temp):
    if temp < 0:
        return "非常に寒いです。厚手のコートや手袋、帽子を着用してください。"
    elif 0 <= temp < 10:
        return "寒いです。コートやセーターを着用してください。"
    elif 10 <= temp < 20:
        return "少し肌寒いです。ジャケットや長袖を着用してください。"
    elif 20 <= temp < 30:
        return "快適な気温です。軽装で大丈夫です。"
    else:
        return "暑いです。Tシャツやショートパンツを着用してください。"

if __name__ == '__main__':
    app.run(debug=True)