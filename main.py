import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from decouple import config

Token = config('TOKEN')

bot = Bot(Token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['meme'])
async def meme(message: types.Message):
    photos = ["photos/meme1.jpg", "photos/meme2.jpg", "photos/meme3.jpg"]
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    next_quiz_button = InlineKeyboardButton("Next", callback_data='Next')
    markup.add(next_quiz_button)

    question = 'Which library is used to program Telegramm bots?'
    answers = [
        'random',
        'aiogram',
        'math',
        'cmath'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        type='quiz',
        correct_option_id=1,
        explanation='Skill Issue',
        reply_markup=markup,
    )


@dp.callback_query_handler(text='Next')
async def next_quiz(call: types.CallbackQuery):
    question = 'Which library provides access to functions for complex numbers?'
    answers = [
        'random',
        'aiogram',
        'math',
        'cmath'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        type='quiz',
        correct_option_id=3,
        explanation='Skill Issue'
    )


@dp.message_handler()
async def echo_square(message: types.Message):
    try:
        num = int(message.text)
        await bot.send_message(message.from_user.id, num ** 2)
    except:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
