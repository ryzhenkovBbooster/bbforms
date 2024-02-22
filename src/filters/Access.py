from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message
from src.admin import read_csv


ADMINS = [5735245657, 2065355593, 461365786]


class Auth(BaseFilter):



    async def __call__(self, message: Message):

        if message.from_user.id not in ADMINS:
            return False
        return True




