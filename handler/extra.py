import random
from aiogram import types, Dispatcher
from config import bot, ADMINS
from data.data_bot import sql_random


async def echo_square(message: types.Message):
    try:
        num = int(message.text)
        await bot.send_message(message.chat.id, num ** 2)
    except:
        if message.text.startswith('game') and message.from_user.id in ADMINS:
            await bot.send_dice(message.chat.id, emoji=random.choice(['⚽', '🏀', '🎯', '🎲', '🎰', '🎳']))
        else:
            await bot.send_message(message.chat.id, message.text)


def register(dp: Dispatcher):
    dp.register_message_handler(sql_random, commands=['random'], commands_prefix='!/')
    dp.register_message_handler(echo_square)
