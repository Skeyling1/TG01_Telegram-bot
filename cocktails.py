import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
from googletrans import Translator
from config import TOKEN, COCKTAIL_API_KEY

translator = Translator()


# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


# получает всю инф. через API
def get_cocktail_info(cocktail_name):
   url = f'https://www.thecocktaildb.com/api/json/v1/{COCKTAIL_API_KEY}/search.php?s={cocktail_name}'
   response = requests.get(url)
   return response.json()


# получает отдельные компоненты через API
def get_cocktail_components(cocktail_name):
   url = f'https://www.thecocktaildb.com/api/json/v1/{COCKTAIL_API_KEY}/search.php?s={cocktail_name}'
   response = requests.get(url)
   cocktail_info = response.json()
   components = []
   for i in range(15):
      if cocktail_info["drinks"][0][f"strIngredient{i+1}"]:
         trans_comp = translator.translate(cocktail_info["drinks"][0][f"strIngredient{i + 1}"], dest='ru')
         components.append(trans_comp.text)
   volums = []
   for i in range(15):
      if cocktail_info["drinks"][0][f"strMeasure{i+1}"]:
         trans_vol = translator.translate(cocktail_info["drinks"][0][f"strMeasure{i + 1}"], dest='ru')
         volums.append(trans_vol.text)
   recipe = []
   for i in range(len(components)):
      try:
         recipe.append(f'{components[i]} - {volums[i]}\n')
      except:
         recipe.append(f'{components[i]} - по вкусу\n')
   recipe_str = "".join(recipe)
   return recipe_str


# получает фото через API
def get_cocktail_photo(cocktail_name):
   url = f'https://www.thecocktaildb.com/api/json/v1/{COCKTAIL_API_KEY}/search.php?s={cocktail_name}'
   response = requests.get(url)
   cocktail_info = response.json()
   url_photo = cocktail_info["drinks"][0]["strDrinkThumb"]
   return url_photo


# Хэндлер для команды /start
@dp.message(CommandStart())
async def start(message: Message):
   await message.answer('Привет! Какой рецепт коктеля Вас интересует?')


# Хэндлер для обработки пользовательского запроса
@dp.message()
async def info(message: Message):
   cocktail_name = message.text
   cocktail_info = get_cocktail_info(cocktail_name)
   cocktail_photo = get_cocktail_photo(cocktail_name)
   info = (f'{cocktail_info["drinks"][0]["strInstructions"]}')
   trans_info = translator.translate(info, dest='ru')
   components = get_cocktail_components(cocktail_name)
   await message.answer_photo(photo=cocktail_photo, caption=f"{trans_info.text}\n{components}")


# Запуск бота
async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())