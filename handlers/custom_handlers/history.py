from utils.misc.user import get_user
from database.SQLite_database import *
from database.models.history import History
from telebot.types import Message
from loader import bot


@bot.message_handler(commands=['history'])
def get_history(message: Message):
    if message.text == '/history':
        with database:
            user = get_user(message)
            all_history = History.select().where(History.user_id == user.user_id)
            for history in all_history:
                bot.send_message(message.chat.id,
                                 f'<b>Дата поиска - {history.timestamp.strftime("%Y-%m-%d %H.%M.%S")}\n'
                                 f'Параметры поиска - {history.command}\n'
                                 f'Цель поиска - {history.city}\n'
                                 f'Выбранная локация - {history.location}.</b>')
