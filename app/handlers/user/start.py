from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.full_name}!')
