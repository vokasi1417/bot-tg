import sqlite3

from aiogram.dispatcher import FSMContext

from aiogram.types import ContentTypes
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from const.const import ADMIN_IDS
from filters.filter import IsAdmin
from keyboards.default import movie, admin_button, new_serial_button
from loader import dp, db, db_c, bot
from utils.misc import rate_limit


@rate_limit(limit=2)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}')
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    if message.from_user.id in ADMIN_IDS:
        reply_markup = admin_button
    else:
        reply_markup = movie
    await message.answer('Стартуем', reply_markup=reply_markup)


@dp.message_handler(Text('Рандомный сериал'))
async def random_serial(message: types.Message):
    list_of_serial = db_c.random_serial_from_db()
    name_of_content = list_of_serial[1]
    overview_of_content = list_of_serial[2]
    picture = list_of_serial[3]
    await message.answer_photo(caption=f'<b>{name_of_content}</b>\n\n{overview_of_content}', photo=picture)


@dp.message_handler(IsAdmin(), Text('Добавить сериал'))
async def adm_button(message: types.Message):
    await message.answer("Добавляем новый сериал", reply_markup=new_serial_button)


@dp.message_handler(IsAdmin(), Text('Вернуться в начало'))
async def adm_button(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Админ меню", reply_markup=admin_button)






