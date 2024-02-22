from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from src.admin import read_csv

class SendFormFilter(BaseFilter):



    async def __call__(self, callback: CallbackQuery):


        data = read_csv('chats.csv')
        for i in data:
            if i['chat_id'] == callback.data:
                return True
        return False


