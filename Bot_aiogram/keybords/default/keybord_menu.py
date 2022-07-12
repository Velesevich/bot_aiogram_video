from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ИП'),
            KeyboardButton(text='Организация'),
        ],
        [
            KeyboardButton(text='НДС'),

        ],[
            KeyboardButton(text='На сайт'),
            KeyboardButton(text='Назад'),
        ]
    ],
    resize_keyboard=True
)