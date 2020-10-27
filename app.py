from utils import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import db, db_c


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    try:
        db.create_table_users()
    except Exception as e:
        print(e)
    print(db.count_users()[0])
    print(db.select_all_users())

    try:
        db_c.create_table_content()
    except Exception as e:
        print(e)
    print(db_c.select_all_content())

    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

