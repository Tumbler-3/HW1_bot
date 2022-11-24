import asyncio
import random
import aioschedule
from aiogram import types, Dispatcher

from config import bot


async def get_id(message: types.Message):
    global user_id
    user_id = message.from_user.id
    await message.answer('wednesday-notification ON')


async def my_dudes():
    photos = ["photos/wednesday/wednesday1.png", "photos/wednesday/wednesday2.png",
              "photos/wednesday/wednesday3.png", "photos/wednesday/wednesday4.png"]
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(chat_id=user_id, photo=photo)


async def it_is_wednesday():
    aioschedule.every().wednesday.at('13:00').do(my_dudes)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(3)


def register(dp: Dispatcher):
    dp.register_message_handler(get_id,
                                lambda word: 'wednesday' in word.text)
