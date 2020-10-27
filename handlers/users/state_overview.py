from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from filters.filter import IsAdmin
from loader import dp
from aiogram import types

from states import Content


@dp.message_handler(IsAdmin(), Text('Описание'))
async def button_overview(message: types.Message):
    await message.answer("Добавляем <b>описание</b> сериала")

    await Content.overview_of_content.set()


@dp.message_handler(state=Content.overview_of_content)
async def answer_overview(message: types.Message, state: FSMContext):
    overview_of_content = message.text

    await state.update_data(overview_of_content=overview_of_content)
    await message.answer(f'Описание сериала принято\nВы ввели описание сериала: <b>{overview_of_content}</b>\nПроверь '
                         f'описание сериала, если хочешь его изменить, то нажми кнопку <b>"Описание"</b>')
    await state.reset_state(with_data=False)
