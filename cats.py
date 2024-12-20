import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_cat_breeds():

async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())