from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_quiz_button = InlineKeyboardButton("Next", callback_data='quiz3')
    markup.add(next_quiz_button)

    question = 'Which library provides access to functions for complex numbers?'
    answers = [
        'random',
        'aiogram',
        'math',
        'cmath'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        type='quiz',
        correct_option_id=3,
        explanation='Skill Issue',
        reply_markup=markup,
    )


async def quiz3(call: types.CallbackQuery):
    question = 'Which library provides access to mathematical tasks?'
    answers = [
        'random',
        'aiogram',
        'math',
        'cmath'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        type='quiz',
        correct_option_id=2,
        explanation='Skill Issue'
    )


def register(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, text='quiz2')
    dp.register_callback_query_handler(quiz3, text='quiz3')
