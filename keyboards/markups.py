from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

save_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton('Yes'),
    KeyboardButton('No')
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('Cancel'))
