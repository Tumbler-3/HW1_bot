from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, ADMINS
from data.data_bot import sql_all, sql_delete


async def pin(message: types.Message):
    if message.from_user.id in ADMINS:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        await bot.send_message(message.chat.id, f'pinned')
    else:
        await bot.send_message(message.chat.id, f"You don't have admin powers")


async def show_all_mentors(message: types.Message):
    if message.from_user.id in ADMINS:
        mentors = await sql_all()
        for mentor in mentors:
            await bot.send_message(message.from_user.id,
                                   f"ID: {mentor[0]}\n"
                                   f"Name: {mentor[1]}\n"
                                   f"Course: {mentor[2]}\n"
                                   f"Age: {mentor[3]}\n"
                                   f"Group: {mentor[4]}\n",
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton(f"delete {mentor[1]}",
                                                            callback_data=f"delete {mentor[0]}"))
                                   )
    else:
        await bot.send_message(message.from_user.id, f"You don't have admin powers")


async def delete(call: types.CallbackQuery):
    await sql_delete(call.data.replace('delete ', ''))
    await bot.delete_message(call.from_user.id, call.message.message_id)


def register(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(show_all_mentors, commands=['mentors'], commands_prefix='!/')
    dp.register_callback_query_handler(delete,
                                       lambda call: call.data and call.data.startswith("delete "))
