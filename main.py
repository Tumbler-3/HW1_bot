from aiogram.utils import executor
from config import dp
from data.data_bot import sql_data
from handler import client, extra, callback, admin, fsm_Admin_Mentor


async def on_startup(_):
    sql_data()


fsm_Admin_Mentor.register(dp)
client.register(dp)
callback.register(dp)
admin.register(dp)
extra.register(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
