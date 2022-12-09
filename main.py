import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN

import database as db

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("👋 Salom barchaga!\n\n🤖 Men Guruhlarda AI (sun'iy intelekt) yordamida suhbatlashuvchi botman\n\nSinab ko'rasmi? Unda meni guruhga qo'shing!")


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
  await message.reply("Meni shunchaki istalgan guruhga qo'shing va albatta adminlikni bering.")



@dp.message_handler()
async def echo(message: types.Message):
  if message.reply_to_message:
    if message.reply_to_message.text:
      db.add_message(message.reply_to_message.text, message.text)

  res = db.get_message(message.text)
  if res:
    await message.answer(res['ans'])


if __name__ == '__main__':
  db.preparate()
  executor.start_polling(dp, skip_updates=True)