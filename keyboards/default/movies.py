from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

movie = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Рандомный сериал")
        ],
    ],
    resize_keyboard=True
)
