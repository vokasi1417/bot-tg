from aiogram.dispatcher.filters.state import State, StatesGroup


class Content(StatesGroup):
    name_of_content = State()
    overview_of_content = State()
    picture_of_content = State()