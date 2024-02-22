import os

from aiogram import Router
import ast
from aiogram.types import Message, CallbackQuery, PollAnswer, InputFile, FSInputFile, File
from aiogram import F
from src.admin import read_csv, delete_csv

from src.filters.Access import Auth, ADMINS
from src.filters.delete_chat import UserAccessFilter
from src.filters.send_form import SendFormFilter

from src.keyboard.index_key import send_to_chat_k, edit_form_key

router = Router()

# @router.message('send_form')
# async def send_form(message: Message):
#     pass



@router.message(F.text.lower() == 'my_id')
async def my_id(message: Message):
    user_id = message.from_user.id
    await message.answer(f'{user_id}')



@router.message(F.text.lower() == 'list chat', Auth())
async def list_chat(message: Message):
    obj_chats = read_csv('chats.csv')
    titles = ', '.join(item['chatname'] for item in obj_chats)
    await message.answer(titles)



@router.message(UserAccessFilter(), Auth())
async def delete_chat(message: Message):
    data = read_csv('chats.csv')
    for i in data:
        if i['chatname'] in message.text:
            chatname = i['chatname']
            delete_csv(i['chat_id'], 'chats.csv')
            await message.bot.leave_chat(chat_id=int(i['chat_id']))

            await message.answer(f'чат - ({chatname})  удален!\nЕсли он удален по ошибке, просто добавьте бота снова в чат')



@router.message(F.text.lower() == 'send form')
async def get_form(message:Message):
    data = read_csv('chats.csv')
    await message.answer('выберите кому отправть ОПРОС', reply_markup=send_to_chat_k(data))

@router.callback_query(SendFormFilter(), Auth())
async def send_form(callback: CallbackQuery):
    data = read_csv('form.csv')
    if data:

        quest = data[0]['вопрос']
        options = ast.literal_eval(data[0]['варианты_ответа'])

        chat_id = callback.data
        return await callback.bot.send_poll(chat_id=int(chat_id), question=quest, options=options,is_anonymous=False )

@router.poll_answer()
async def poll_answer( poolAnswer: PollAnswer):
    data = read_csv('form.csv')
    if data:

        pol_id = poolAnswer.option_ids
        response = data[0]['варианты_ответа']
        response = ast.literal_eval(response)
        text = (f'Пользователь @{poolAnswer.user.username}\n'
                f'Ответил на опрос: {response[pol_id[0]]}')
        for i in ADMINS:
            await poolAnswer.bot.send_message(chat_id=i, text=text )


@router.message(F.text.lower() == 'edit form',Auth())
async def get_form(message: Message):
    curren_file = os.getcwd()
    # print('[PATH] ', curren_file)
    path_to_file = f'form.csv'
    await message.answer_document(FSInputFile(path_to_file))

@router.message(F.document)
async def upload_form(message: Message):

    document_id = message.document.file_id
    file = await message.bot.get_file(document_id)
    file_path = file.file_path
    curren_file = os.getcwd()

    await message.bot.download_file(file_path, message.document.file_name)

    await message.answer('complete')

@router.message(F.text.lower() == 'help')
async def get_help(message: Message):
    await message.answer('Что бы начать отправлять опросы в чат, просто добавьте бота в чат\n'
                         '[send form] - Отправить опрос в чат.\n'
                         '[edit form] - Получить файл с опросом, для редактирования. Важно, не менять структуру файла, тип или название\n'
                         '[delete ИМЯ ЧАТА] - Команда удалит чат из базы, бот выйдет из чата')

# @router.callback_query(Auth())
# async def edit_form(callback: CallbackQuery):
#     data = read_csv('form.csv')
#     options = ast.literal_eval(data[0]['варианты_ответа'])
#     quest = data[0]['вопрос']
#
#     if callback.data == 'вопрос':
#         quest
#     if len(callback.data) <= 1:
#         pass