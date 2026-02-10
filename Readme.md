# Telegram AI Bot with Docker

Бот на базе AI для Telegram с поддержкой контекста, историей сообщений и интеграцией с OpenAI-совместимыми API (OpenRouter).


### 1. Запуск с Docker

# Клонируй репозиторий
git clone https://github.com/levvis16/telegram-ai-bot


# Собрать и запустить одним командой
docker-compose up -d --build

# Проверить работу
docker-compose logs --tail=20


### Локальный запуск

# Создать виртуальное окружение
python -m venv venv

# Активировать (Windows)
venv\Scripts\activate

# Активировать (Linux/macOS)
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Запустить бота
python main.py