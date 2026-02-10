import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
CONTEXT_LIMIT = int(os.getenv("CONTEXT_LIMIT", 15))
DB_PATH = os.getenv("DB_PATH", "/app/data/bot_history.db")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен в .env файле")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY не установлен в .env файле")