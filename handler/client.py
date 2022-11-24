import random
import time
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def meme(message: types.Message):
    photos = ["photos/memes/meme1.jpg", "photos/memes/meme2.jpg", "photos/memes/meme3.jpg"]
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    next_quiz_button = InlineKeyboardButton("Next", callback_data='quiz2')
    markup.add(next_quiz_button)

    question = 'Which library is used to program Telegramm bots?'
    answers = [
        'random',
        'aiogram',
        'math',
        'cmath'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        type='quiz',
        correct_option_id=1,
        explanation='Skill Issue',
        reply_markup=markup,
    )


async def dice(message: types.Message):
    await bot.send_message(message.chat.id, f'Your dice')
    dice1 = await bot.send_dice(message.chat.id, emoji='🎲')
    time.sleep(3.5)

    await bot.send_message(message.chat.id, f'My dice')
    dice2 = await bot.send_dice(message.chat.id, emoji='🎲')
    time.sleep(3.5)

    if dice1.dice.value > dice2.dice.value:
        await bot.send_message(message.chat.id, f'{dice1.dice.value}:{dice2.dice.value} - You won')
    elif dice1.dice.value < dice2.dice.value:
        await bot.send_message(message.chat.id, f'{dice1.dice.value}:{dice2.dice.value} - I won')
    else:
        await bot.send_message(message.chat.id, f'{dice1.dice.value}:{dice2.dice.value} - Draw')


def register(dp: Dispatcher):
    dp.register_message_handler(quiz1, commands=['quiz'], commands_prefix='!/')
    dp.register_message_handler(meme, commands=['meme'], commands_prefix='!/')
    dp.register_message_handler(dice, commands=['dice'], commands_prefix='!/')
