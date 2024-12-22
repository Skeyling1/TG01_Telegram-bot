import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random
import requests
from datetime import datetime, timedelta

from config import TOKEN, COCKTAIL_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()


def get_cocktail_info(cocktail_name):
   url = f'https://www.thecocktaildb.com/api/json/v1/{COCKTAIL_API_KEY}/search.php?s={cocktail_name}'
   response = requests.get(url)
   return response.json()




@dp.message(CommandStart())
async def start(message: Message):
   await message.answer('Привет! Какой рецепт коктеля Вас интересует?')


@dp.message()
async def info(message: Message):
   cocktail_name = message.text
   cocktail_info = get_cocktail_info(cocktail_name)
   info = (f'{cocktail_info["drinks"][0]["strInstructions"]}')
   await message.answer(info)





async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())