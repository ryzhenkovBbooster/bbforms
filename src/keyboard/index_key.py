import json

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def send_to_chat_k(data: list[dict]):
    rows = [[InlineKeyboardButton(text=item['chatname'], callback_data=item['chat_id'])] for item in data]
    return InlineKeyboardMarkup(inline_keyboard=rows)



def edit_form_key(option: list, quest: str):
    rows = [[InlineKeyboardButton(text=item, callback_data=str(option.index(item)))] for item in option]
    rows.insert(0,[InlineKeyboardButton(text=quest, callback_data='вопрос')])


    return InlineKeyboardMarkup(inline_keyboard=rows)



