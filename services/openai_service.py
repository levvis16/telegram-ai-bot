import requests
import json
from config import OPENAI_API_KEY, MODEL_NAME

def generate_response(messages):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",  # OpenRouter требует
            "X-Title": "Telegram Bot"
        }
        
        data = {
            "model": MODEL_NAME,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1024
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        if response.status_code != 200:
            return f"Ошибка API: {response.status_code} - {response.text}"
        
        result = response.json()
        
        if "choices" not in result or not result["choices"]:
            return "API вернул пустой ответ"
            
        return result["choices"][0]["message"]["content"]
        
    except Exception as e:
        return f"Ошибка: {str(e)}"
