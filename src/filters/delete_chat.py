from aiogram.filters import BaseFilter
from aiogram.types import Message
from src.admin import read_csv

class UserAccessFilter(BaseFilter):



    async def __call__(self, message: Message):

        if 'delete' not in str(message.text):
            return False
        data = read_csv('chats.csv')
        text = message.text.replace('delete ', '')
        for i in data:
            if i['chatname'] == text:
                return True
        return False


