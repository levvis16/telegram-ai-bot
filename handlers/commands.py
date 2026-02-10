from aiogram import Router, types, F
from aiogram.filters import Command
from services.database import clear_history
from utils.keyboards import get_main_kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await clear_history(message.from_user.id)
    text = ('добрый день, это онлайн консультант\n'
            'чем я могу вам помочь?'
            )
    await message.answer(text, reply_markup=get_main_kb(), parse_mode="Markdown")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = ("За помощью обратитесь к @Levvis22")
    await message.answer(help_text, parse_mode="Markdown")

@router.message(F.text == "Новый запрос")
async def btn_reset(message: types.Message):
    await clear_history(message.from_user.id)
    await message.answer("контекст очищен, что обсудим?")

