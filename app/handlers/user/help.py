from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from utils.misc import rate_limit

from loader import dp


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(msg: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку'
    ]
    await msg.answer('\n'.join(text))
