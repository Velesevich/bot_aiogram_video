from aiogram import types
from loader import dp

@dp.message_handler(text='/start')
async def soobschrnie(message:types.Message):
    await message.answer('получил ')
    name=message.from_user.full_name
    users_id=message.from_user.id
    print('Name ', name, users_id)