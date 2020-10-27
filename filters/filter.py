from aiogram.dispatcher.filters import Filter
from aiogram.types import Message

from const.const import ADMIN_IDS


class IsAdmin(Filter):

    async def check(self, message: Message, *args) -> bool:
        return message.from_user.id in ADMIN_IDS
