from telebot.types import Message
from utils.misc.user import get_user
from utils.misc.distance import distance
from loader import bot
from database.SQLite_database import *


def min_price(message: Message):
    if message.text.isdigit():
        with database:
            user = get_user(message)
            user.min_price = message.text
            user.save()
        bot.send_message(message.chat.id, '<b>Введите максимальную цену за номер.</b>')
        bot.register_next_step_handler(message, max_price)
    else:
        bot.send_message(message.chat.id, '<b>Введите минимальную цену цифрами.</b>')
        bot.register_next_step_handler(message, min_price)


def max_price(message: Message):
    if message.text.isdigit():
        with database:
            user = get_user(message)
            user.max_price = message.text
            user.save()
        bot.send_message(message.chat.id, '<b>Введите максимальное расстояние от центра.</b> (целое число)')
        bot.register_next_step_handler(message, distance)
    else:
        bot.send_message(message.chat.id, '<b>Введите максимальную цену цифрами.</b>')
        bot.register_next_step_handler(message, max_price)
