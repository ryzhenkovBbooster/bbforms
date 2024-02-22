from aiogram import Router
from aiogram.enums import ChatType
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from aiogram.types import Message
from src.admin import add_chat
router = Router()

@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> IS_MEMBER))
async def update_chat(message: Message):
    if message.chat.type == ChatType.PRIVATE:
        return ''
    chat_id = message.chat.id
    title = message.chat.title
    res = add_chat(chat_id, title)
    if res:
        await message.answer('Привет, теперь я знаю про чат')
    else:
        await message.answer('Я ранее был в этом чате, либо произошла ошибка при добавлении в чат')