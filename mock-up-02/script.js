document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');

    const apiKey = 'YOUR_API_KEY'; // ここにOpenWeatherMapのAPIキーを入力

    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const city = userInput.value.trim();
        
        if (city) {
            addMessage(city, 'user');
            userInput.value = '';

            fetchWeather(city);
        }
    });

    function addMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const avatar = document.createElement('div');
        avatar.className = 'avatar';
        avatar.textContent = sender === 'user' ? 'You' : 'AI';

        const content = document.createElement('div');
        content.className = 'message-content';
        content.textContent = message;

        messageDiv.appendChild(avatar);
        messageDiv.appendChild(content);
        
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }

    function fetchWeather(city) {
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=ja`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data.cod === 200) {
                    const weather = data.weather[0].description;
                    const temp = data.main.temp;
                    const message = `${city}の天気は${weather}で、気温は${temp}℃です。`;
                    addMessage(message, 'bot');
                } else {
                    addMessage('都市が見つかりませんでした。もう一度お試しください。', 'bot');
                }
            })
            .catch(error => {
                console.error('Error fetching weather data:', error);
                addMessage('天気情報を取得できませんでした。後でもう一度お試しください。', 'bot');
            });
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});