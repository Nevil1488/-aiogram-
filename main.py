import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from models import async_main
from handlers import router

async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == "__main__":

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')