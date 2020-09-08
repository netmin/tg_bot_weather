import logging

import aiohttp
from aiogram import types

# Configure logging
from loader import dp

logging.basicConfig(level=logging.INFO)


async def on_startup(db):
    import filters
    import middlewares
    import handlers
    filters.setup(db)
    middlewares.setup(db)
    handlers.user.setup(db)

    from utils.notify_admins import on_startup_notify
    from utils.set_bot_commands import set_default_commands
    await on_startup_notify(db)
    await set_default_commands(db)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import user
    executor.start_polling(dp, on_startup=on_startup)

