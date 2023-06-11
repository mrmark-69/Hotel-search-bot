from telebot.types import Message
from utils.misc.target import send_target
from utils.misc.user import get_user
from loader import bot
from database.SQLite_database import *


@bot.message_handler(commands=['highprice'])
def command(message: Message):
    if message.text == '/highprice':
        with database:
            user = get_user(message)
            user.command = message.text
            user.max_price = 9999
            user.save()
    bot.send_message(message.chat.id, '<b>Введите пункт назначения.</b>')
    bot.register_next_step_handler(message, send_target)