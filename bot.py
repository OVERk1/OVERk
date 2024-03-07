import asyncio
import handlers

from aiogram import types, Bot, Dispatcher, F, Router

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command, StateFilter

from config_reader import config



async def main():

    storage = MemoryStorage()
    
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher(bot=bot, storage=storage)


    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())