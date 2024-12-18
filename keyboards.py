from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

reply_kb_test = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тестовая кнопка 1")],
    [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)

inline_kb_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
    [InlineKeyboardButton(text="Новости", callback_data='news')],
    [InlineKeyboardButton(text="Профиль", callback_data='person')]
])







test = ["кнопка1", "кнопка2", "кнопка3", "кнопка4"]



async def test_keyboard():
    keyboard = ReplyKeyboardBuilder()
    for key in test:
        keyboard.add(KeyboardButton(text=key))
    return keyboard.adjust(2).as_markup()