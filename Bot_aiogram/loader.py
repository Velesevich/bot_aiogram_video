from aiogram import Bot, Dispatcher, types


from data import config

bot = Bot(token=config.BOT_TOKEN)

# Создание диспетчера
dp=Dispatcher (bot)