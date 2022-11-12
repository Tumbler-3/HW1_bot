from aiogram import types, Dispatcher
from config import bot, ADMINS


async def pin(message: types.Message):
    if message.from_user.id in ADMINS:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        await bot.send_message(message.chat.id, f'pinned')
    else:
        await bot.send_message(message.chat.id, f"You don't have admin powers")


def register(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
