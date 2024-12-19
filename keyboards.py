from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

reply_kb_test = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тестовая кнопка 1")],
    [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)


inline_kb_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url='https://edition.cnn.com')],
    [InlineKeyboardButton(text="Музыка", url='https://music.yandex.ru/home')],
    [InlineKeyboardButton(text="Видео", url='https://youtu.be/iTZCZK8wgdE')]
])


inline_hi_bye = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Привет", callback_data='hi')],
    [InlineKeyboardButton(text="Пока", callback_data='bye')]
])


inline_dynamic = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='show_more_buttons')]
])


test = ["Опция 1", "Опция 2"]


async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    # for key in test:
    #     keyboard.add(InlineKeyboardButton(text=key, callback_data=))
    keyboard.add(InlineKeyboardButton(text="Опция 1", callback_data='option1'))
    keyboard.add(InlineKeyboardButton(text="Опция 2", callback_data='option2'))
    return keyboard.adjust(2).as_markup()