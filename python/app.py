from flask import Flask, render_template, request, jsonify
from weather_api import WeatherAPI
from coordinate_ai import CoordinateAI

app = Flask(__name__)
weather_api = WeatherAPI()
coordinate_ai = CoordinateAI()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = weather_api.get_weather(city)
        
        if weather_data:
            coordinate = coordinate_ai.get_coordinate(weather_data)
            return render_template('index.html', 
                                weather=weather_data, 
                                coordinate=coordinate,
                                city=city)
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

