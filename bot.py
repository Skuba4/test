from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import commands
import asyncio

bot = Bot(TOKEN, timeout=10)
dp = Dispatcher()


async def main():
    dp.include_router(commands.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
