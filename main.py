import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from services.database import init_db
from handlers import commands, chat

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    await init_db()

    dp.include_router(commands.router)
    dp.include_router(chat.router)

    logging.info("бот запущен")
    try:
        await dp.start_polling(bot)
    finally:
        logging.info("остановка бота")
        await bot.session.close()
        
if __name__ == '__main__':
    asyncio.run(main())