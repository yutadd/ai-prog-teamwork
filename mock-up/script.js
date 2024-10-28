document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');

    // モックの応答データ
    const mockResponses = [
        {
            type: 'text',
            content: "なるほど、理解しました。詳しく教えていただけますか？"
        },
        {
            type: 'text',
            content: "申し訳ありません。その質問については現在対応できません。"
        },
        {
            type: 'text',
            content: "はい、お手伝いさせていただきます。具体的に何をお探しですか？"
        },
        {
            type: 'text',
            content: "興味深い質問ですね。もう少し具体的に説明していただけますか？"
        }
    ];

    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const message = userInput.value.trim();
        
        if (message) {
            // ユーザーメッセージを追加
            addMessage(message, 'user');
            userInput.value = '';

            // 入力中表示
            showTypingIndicator();

            // ボットの応答を遅延
            setTimeout(() => {
                removeTypingIndicator();
                const response = mockResponses[Math.floor(Math.random() * mockResponses.length)];
                addMessage(response.content, 'bot');
            }, 1500);
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

    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'typing-indicator';
        typingDiv.id = 'typing-indicator';
        
        const avatar = document.createElement('div');
        avatar.className = 'avatar';
        avatar.textContent = 'AI';

        const dots = document.createElement('div');
        dots.className = 'dots';
        dots.innerHTML = `
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
        `;

        typingDiv.appendChild(avatar);
        typingDiv.appendChild(dots);
        
        chatMessages.appendChild(typingDiv);
        scrollToBottom();
    }

    function removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Enterキーでフォーム送信
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            chatForm.dispatchEvent(new Event('submit'));
        }
    });
});