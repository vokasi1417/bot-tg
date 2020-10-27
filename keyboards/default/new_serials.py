from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

new_serial_button = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Название")
        ],
    [
            KeyboardButton("Описание")
        ],
    [
            KeyboardButton("Картинка")
        ],
    [
            KeyboardButton("Сохранить")
        ],
    [
            KeyboardButton("Вернуться в начало")
        ],

    ],
    resize_keyboard=True
)