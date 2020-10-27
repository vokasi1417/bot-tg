from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.data_base_of_users import DataBaseOfUsers
from utils.db_api.database_of_content import DataBaseOfContent

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = DataBaseOfUsers()
db_c = DataBaseOfContent()