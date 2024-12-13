import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
import random
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://img.freepik.com/free-vector/hand-drawn-valentine-s-day-cats-couple_23-2148398963.jpg?semt=ais_hybrid', 'https://img.freepik.com/free-vector/flat-cute-animal-cat-space-illustration-kids-cute-cat-character_69135-1249.jpg?semt=ais_hybrid', 'https://img.freepik.com/free-vector/cute-valentine-s-day-animal-couple_23-2148390534.jpg?semt=ais_hybrid']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='это супер крутая картинка')

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого какая фотка!', 'непонятно что это', 'не отправляй такое больше!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(Command('weather'))
async def weather(message: Message):
    city = 'London'
    api_key = "ваш токен"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric"
    request = requests.get(url)
    weather = request.json()
    temp = str(weather['main']['temp'])
    await message.answer(f"Температура в городе {city} составляет {temp} °C")


@dp.message(F.text == "Что такое ИИ?")
async def ai_text(message: Message):
    await message.answer('Иску́сственный интелле́кт (англ. artificial intelligence; AI) в самом широком смысле — это интеллект, демонстрируемый машинами, в частности компьютерными системами.')


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /photo \n /weather')

@dp.message(CommandStart)
async def start(message: Message):
    await message.answer('Приветики! Я бот!')


async def main():
    await dp.start_polling(bot)


if __name__ =='__main__':
    asyncio.run(main())