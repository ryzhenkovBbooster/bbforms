import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from src import bot_update, client

load_dotenv()

dp = Dispatcher()

async def main() -> None:
    dp.include_routers(bot_update.router, client.router)
    bot = Bot(os.getenv("TOKEN"))

    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())