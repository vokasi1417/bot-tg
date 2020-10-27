from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ContentTypes
from filters.filter import IsAdmin
from loader import dp, db_c
from aiogram import types

from states import Content


@dp.message_handler(IsAdmin(), Text('Картинка'))
async def button_picture(message: types.Message):
    await message.answer("Добавляем <b>картинку</b> сериала")

    await Content.picture_of_content.set()


@dp.message_handler(state=Content.picture_of_content, content_types=ContentTypes.PHOTO)
async def answer_picture(message: types.Message, state: FSMContext):
    picture_id = message.photo[0].file_id
    await state.update_data(picture=picture_id)
    await message.answer('Картинка получена')
    await state.reset_state(with_data=False)


@dp.message_handler(IsAdmin(), Text('Сохранить'))
async def button_overview(message: types.Message, state: FSMContext):
    serial_data = await state.get_data()
    name_of_content = serial_data['name_of_content']
    overview_of_content = serial_data['overview_of_content']
    picture = serial_data['picture']
    db_c.add_content(name_of_content=name_of_content, overview_of_content=overview_of_content, picture=picture)
    await state.reset_state()
    await message.answer("Сохранили сериал")
