from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_button = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Добавить сериал")
        ],
    [
            KeyboardButton("Рандомный сериал")
        ],
    ],
    resize_keyboard=True
)