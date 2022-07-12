from aiogram import types
from loader import dp

@dp.message_handler(text='ИП')
async def buttons_test(message:types.Message):
    await message.answer('Вы являетесь ИП')

@dp.message_handler(text='Организация')
async def buttons_test(message:types.Message):
    await message.answer('Вы являетесь Организацией')

@dp.message_handler(text='На сайт')
async def buttons_test(message: types.Message):
    await message.answer('Идем на сайт')