from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from filters.filter import IsAdmin
from loader import dp
from aiogram import types

from states import Content


@dp.message_handler(IsAdmin(), Text('Название'))
async def button_name(message: types.Message):
    await message.answer("Добавляем <b>название</b> сериала")

    await Content.name_of_content.set()


@dp.message_handler(state=Content.name_of_content)
async def answer_name(message: types.Message, state: FSMContext):
    name_of_content = message.text

    await state.update_data(name_of_content=name_of_content)
    await message.answer(f"Название сериала принято\nВы ввели название сериала: <b>{name_of_content}</b>\nПроверь "
                         f"название сериала, если хочешь его изменить, то нажми кнопку <b>\"Название\"</b>")
    await state.reset_state(with_data=False)










