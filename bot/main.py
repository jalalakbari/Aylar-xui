from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
import asyncio
import logging
import json
from bot.handlers import start_handler, user_handler, admin_handler, owner_handler, callback_queries

# بارگذاری config
with open("bot/config.json") as f:
    config = json.load(f)

bot = Bot(token=config["bot_token"], parse_mode=ParseMode.HTML)
dp = Dispatcher()

# ثبت هندلرها
start_handler.register(dp)
user_handler.register(dp)
admin_handler.register(dp)
owner_handler.register(dp)
callback_queries.register(dp)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
