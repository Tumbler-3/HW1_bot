from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from config import ADMINS, bot
from data.data_bot import sql_add
from keyboards.markups import save_markup, cancel_markup


class FSMRegistration(StatesGroup):
    id = State()
    name = State()
    course = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        await FSMRegistration.id.set()
        await message.answer("What's Your mentor's id?", reply_markup=cancel_markup)
    elif message.chat.type == 'public' and message.from_user.id in ADMINS:
        await message.answer("DM me")
    else:
        await message.answer("You don't have admin powers")


async def get_id(message: types.Message, state: FSMContext):
    try:
        num = int(message.text)
        async with state.proxy() as data:
            data['id'] = num
            await FSMRegistration.next()
            await message.answer("What's Your mentor's name?", reply_markup=cancel_markup)
    except:
        await message.answer("Write numbers only")


async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMRegistration.next()
    await message.answer("What's Your mentor's course?", reply_markup=cancel_markup)


async def get_course(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['course'] = message.text
    await FSMRegistration.next()
    await message.answer("What's Your mentor's age?", reply_markup=cancel_markup)


async def get_age(message: types.Message, state: FSMContext):
    try:
        num = int(message.text)
        async with state.proxy() as data:
            data['age'] = num
        await FSMRegistration.next()
        await message.answer("What's Your mentor's group?", reply_markup=cancel_markup)
    except:
        await message.answer("Write number only")


async def get_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await bot.send_message(message.from_user.id,
                           f"ID: {data['id']}"
                           f"Name: {data['name']}"
                           f"Course: {data['course']}"
                           f"Age: {data['age']}"
                           f"Group: {data['group']}")
    await FSMRegistration.next()
    await message.answer("Do you want save it?", reply_markup=save_markup)


async def yes_no(message: types.Message, state: FSMContext):
    if message.text.lower() == 'yes':
        await message.answer("Saved")
        await sql_add(state)
        await state.finish()
    elif message.text.lower() == 'no':
        await message.answer("Didn't save")
        await state.finish()
    else:
        await message.answer("Yes or No?")


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Canceled")


def register(dp: Dispatcher):
    dp.register_message_handler(cancel, state='*', commands=['cancel'])
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['reg'], commands_prefix='!/')
    dp.register_message_handler(get_id, state=FSMRegistration.id)
    dp.register_message_handler(get_name, state=FSMRegistration.name)
    dp.register_message_handler(get_course, state=FSMRegistration.course)
    dp.register_message_handler(get_age, state=FSMRegistration.age)
    dp.register_message_handler(get_group, state=FSMRegistration.group)
    dp.register_message_handler(yes_no, state=FSMRegistration.submit)
