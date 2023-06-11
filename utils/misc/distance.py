from telebot.types import Message
from utils.misc.distance_outputs import *
from loader import bot


def distance(message: Message):
    if message.text.isdigit():
        with database:
            user = get_user(message)
            user.distance = message.text
            user.save()
            if user.photo_num > 0:
                distance_output_photo(bot=bot, message=message)
            else:
                distance_output(bot=bot, message=message)
    else:
        bot.send_message(message.chat.id, '<b>Введите расстояние до центра цифрами.</b>')
        bot.register_next_step_handler(message, distance)
