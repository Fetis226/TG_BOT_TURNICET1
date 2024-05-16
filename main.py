import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import Send
import handlers
from BD import parent_log_reg, rassilka, entry, check
from aiogram.filters.command import Command
from aiogram.types import Message
from config_reader import config
from handlers import router
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
async def main():
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.include_router(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
async def on_startup():
    asyncio.create_task(Send(types, bot))

if __name__ == "__main__":
     asyncio.run(main())
