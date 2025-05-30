"""
Stage1:
- Меню с кнопками
    - Создать заказ - Доставка/Самовывоз- Оплата заказа
    - Корзина заказаов
    - Статус заказа(в процессе/готов/доставлен)

Stage2:
-Отделить хендлеры с помощью роутингов в папку handlers
"""
import asyncio
import logging
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F

load_dotenv()
api_key = os.getenv("BOT_API_KEY")


bot = Bot(token=api_key)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    user_name = message.from_user.full_name
    kb = [
        [types.KeyboardButton(text="Статус заказа")],
        [types.KeyboardButton(text="Создать заказ")],
        [types.KeyboardButton(text="Корзина заказов")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
    )
    await message.reply(f"Привет, {user_name}!\n", reply_markup=keyboard)

@dp.message(F.text.lower() == "Статус заказа")
async def with_puree(message: types.Message):
    await message.reply("Выберите заказ")

@dp.message(F.text.lower() == "Создать заказ")
async def with_puree(message: types.Message):
    await message.reply("Выберите блюдо")

@dp.message(F.text.lower() == "Корзина заказов")
async def without_puree(message: types.Message):
    await message.reply("Список заказов")


async def main():
  await dp.start_polling(bot)

if __name__ == '__main__':
  #logging.basicConfig(level=logging.INFO)# Использовать только при дебаггинге, на  прод не выливать, будет тормозить все
  #try:
    asyncio.run(main())
  #except KeyboardInterrupt:
   #print('Exit')