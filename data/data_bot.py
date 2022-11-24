import random
import sqlite3
from aiogram import types
from config import bot


def sql_data():
    global db, cursor
    db = sqlite3.connect('mentor_data.sqlite3')
    cursor = db.cursor()

    if db:
        db.execute("CREATE TABLE IF NOT EXISTS mentors"
                   "(id INTEGER PRIMARY KEY, name TEXT NOT NULL,"
                   "course TEXT, age INTEGER, grupp TEXT)")
        db.commit()


async def sql_add(state):
    try:
        async with state.proxy() as data:
            cursor.execute("INSERT INTO mentors VALUES "
                           "(?, ?, ?, ?, ?)", tuple(data.values()))
            db.commit()
    except sqlite3.Error as e:
        print(e)


async def sql_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_random(message: types.Message):
    result = await sql_all()
    random_user = random.choice(result)
    await bot.send_message(message.from_user.id,
                           f"ID: {random_user[0]}\n"
                           f"Name: {random_user[1]}\n"
                           f"Course: {random_user[2]}\n"
                           f"Age: {random_user[3]}\n"
                           f"Group: {random_user[4]}\n")


async def sql_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()


async def sql_all_ids():
    return cursor.execute("SELECT id FROM mentors").fetchall()
