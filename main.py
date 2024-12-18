import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN
import random
import requests
from gtts import gTTS
import os
from googletrans import Translator
import keyboards as kb


translator = Translator()

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://img.freepik.com/free-vector/hand-drawn-valentine-s-day-cats-couple_23-2148398963.jpg?semt=ais_hybrid',
            'https://img.freepik.com/free-vector/flat-cute-animal-cat-space-illustration-kids-cute-cat-character_69135-1249.jpg?semt=ais_hybrid',
            'https://img.freepik.com/free-vector/cute-valentine-s-day-animal-couple_23-2148390534.jpg?semt=ais_hybrid']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='это супер крутая картинка')


@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile("video.mp4")
    await bot.send_video(message.chat.id, video)


@dp.message(Command('audio'))
async def audio(message: Message):
    audio = FSInputFile("tweet_001.mp3")
    await bot.send_audio(message.chat.id, audio)


@dp.message(Command('voice'))
async def audio(message: Message):
    voice = FSInputFile("detskiy.ogg")
    await message.answer_voice(voice)


@dp.message(Command('training'))
async def training(message: Message):
   training_list = [
       "Тренировка 1: Скручивания: 3 подхода по 15 повторений. Велосипед: 3 подхода по 20 повторений (каждая сторона). Планка: 3 подхода по 30 секунд",
       "Тренировка 2: Подъемы ног: 3 подхода по 15 повторений. Русский твист: 3 подхода по 20 повторений (каждая сторона). Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
       "Тренировка 3: Скручивания с поднятыми ногами: 3 подхода по 15 повторений. Горизонтальные ножницы: 3 подхода по 20 повторений. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
   ]
   rand_tr = random.choice(training_list)
   await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")
   tts = gTTS(text=rand_tr, lang='ru')
   tts.save("training.ogg")
   audio = FSInputFile('training.ogg')
   await bot.send_voice(message.chat.id, audio)
   os.remove("training.ogg")


@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile("TG02.pdf")
    await bot.send_document(message.chat.id, doc)


@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого какая фотка!', 'непонятно что это', 'не отправляй такое больше!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')


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


@dp.message(F.text == "Тестовая кнопка 1")
async def test_button(message: Message):
   await message.answer('Обработка нажатия на reply кнопку')


@dp.callback_query(F.data == "news")
async def news(callback: CallbackQuery):
    await callback.answer("загрузка новостей", show_alert=True)
    await callback.message.answer('Вот свежие новости')



@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.inline_kb_test)


@dp.message()
async def mes_to_en(message: Message):
    trans_echo = translator.translate(message.text)
    print(trans_echo.text)
    await message.answer(trans_echo.text)

# @dp.message()
# async def test(message: Message):
#     if message.text.lower() == 'тест':
#         await message.answer('тестируем')
#если переставить выше - остальное перестает работать


async def main():
    await dp.start_polling(bot)


if __name__ =='__main__':
    asyncio.run(main())