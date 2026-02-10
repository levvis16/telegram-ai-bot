from aiogram import Router, types
from aiogram.filters import Command
from config import CONTEXT_LIMIT
from services.database import add_message, get_history, clear_history
from services.openai_service import generate_response

router = Router()

@router.message()
async def handle_message(message: types.Message):
    if not message.text:
        return
    
    user_id = message.from_user.id
    
    # Добавляем сообщение пользователя
    await add_message(user_id, "user", message.text)
    
    # Показываем "печатает..."
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    # Получаем историю
    history = await get_history(user_id, CONTEXT_LIMIT)
    
    # Формируем сообщения для API
    messages_for_api = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    for msg in history:
        messages_for_api.append({
            "role": msg["role"], 
            "content": msg["content"]
        })
    
    # Генерируем ответ (БЕЗ await!)
    response_text = generate_response(messages_for_api)
    
    # Сохраняем ответ ассистента
    await add_message(user_id, "assistant", response_text)
    
    # Отправляем ответ
    await message.answer(response_text)


# Хендлер для /clear команды
@router.message(Command("clear"))
async def cmd_clear(message: types.Message):
    await clear_history(message.from_user.id)
    await message.answer("История очищена. Начнём новый диалог!")