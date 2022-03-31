import asyncio, logging, requests, config, sys

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

logging.basicConfig(level=logging.INFO)
version = 1.0
bot = Bot(token=config.token)
dp = Dispatcher(bot)

args = sys.argv
if args:
    for i in range(0, len(args)):
        if args[i] == '-v':
            with open('version.txt', 'w') as f:
                exit()


@dp.message_handler(commands=['leave'])
@dp.message_handler(content_types=["left_chat_member"])
async def leave(message):
    await bot.send_message(message.chat.id, emojize(f'goodbye... ||@{message.from_user.username}||:sad:'))
    await message.delete()


@dp.message_handler(content_types=["photo"])
async def photo_echo(message: types.Message):
    document_id = message.photo[0].file_id
    file_info = await bot.get_file(document_id)
    print(file_info.file_id)
    # await bot.send_chat_action(message.chat.id, action='upload_document')
    file_info = await bot.get_file(document_id)
    await bot.send_photo(message.chat.id, file_info.file_id, caption='Эхо')


@dp.message_handler(content_types=["voice"])
async def audio_echo(message: types.Message):
    document_id = message.voice.file_id
    file_info = await bot.get_file(document_id)
    print(file_info.file_id)
    print(f'http://api.telegram.org/file/bot{config.token}/{file_info.file_path}')
    await bot.send_voice(message.chat.id, file_info.file_id, caption='Эхо')


@dp.message_handler(commands=['start'])
@dp.message_handler(content_types=["new_chat_members"])
async def start(message):
    await bot.send_photo(message.chat.id,
                         'AgACAgIAAxkBAAPnYkSzzJoyFEc0daVXxsQkez-7RL4AAn3LMRv3biFKFXqo3T3PWysBAAMCAANzAAMjBA',
                         caption=f'hello @{message.from_user.username}')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
