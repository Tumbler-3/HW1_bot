from aiogram.utils import executor
from config import dp
from handler import client, extra, callback, admin


client.register(dp)
callback.register(dp)
admin.register(dp)
extra.register(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

