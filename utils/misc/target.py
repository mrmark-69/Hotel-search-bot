from telebot.types import Message
from utils.misc.user import get_user
from keyboards.inline.yes_no_city import get_answer
from loader import bot
from database.SQLite_database import *


def send_target(message: Message):
    target = message.text
    with database:
        user = get_user(message)
        user.city = message.text
        user.save()
    bot.send_message(message.chat.id, f'<b>Вы ищете {target}?</b>', reply_markup=get_answer())
