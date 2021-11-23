from aiogram import Bot, Dispatcher, executor, types
import requests
import json
import logging

API_TOKEN = 'TOKEN'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    with open('20211123_182948.png', 'rb') as photo:
        await message.reply_photo(photo, caption="Assalomu Alaykum👋\n🔐Password Nechi Xonali Bo'sin???\n💡Masalan: 10\n✅Natija: 3cOv8$s#4@")
        
@dp.message_handler()
async def send_Password(message: types.Message):
	text = message.text
	url = 'https://passwordinator.herokuapp.com/generate?num=true&char=true&caps=true&len='+text
	response = requests.get(url)
	rest = json.loads(response.text)
	result = rest['data']
	form = "Password 👉 {}".format(result)
	await bot.send_message(message.chat.id, form)
	

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
#Dasturchining Telegram Manzili: @Python_Koders