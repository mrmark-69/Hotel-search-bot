from telebot.types import Message
from utils.misc.user import get_user
from utils.misc.low_outputs import low_output_photo
from utils.misc.high_outputs import high_output_photo
from utils.misc.price import min_price
from loader import bot
from database.SQLite_database import *


def get_photo(message: Message):
    if message.text.isdigit():
        if int(message.text) > 10:
            message.text = '10'
            bot.send_message(message.chat.id,
                             f'<b>Максимальное количество фото - 10. Будет показано по {message.text} фото.</b>')
            with database:
                user = get_user(message)
                user.photo_num = 10
                command = user.command
                user.save()
            if command == '/highprice':
                high_output_photo(bot=bot, message=message)
            elif command == '/lowprice':
                low_output_photo(bot=bot, message=message)
            elif command == '/bestdeal':
                msg = bot.send_message(message.chat.id, '<b>Введите минимальную цену за номер</b>')
                bot.register_next_step_handler(msg, min_price)
        else:
            with database:
                user = get_user(message)
                user.photo_num = int(message.text)
                command = user.command
                user.save()
            bot.send_message(message.chat.id,
                             f'<b>Будет показано по {message.text} фото.</b>')
            if command == '/highprice':
                high_output_photo(bot=bot, message=message)
            elif command == '/lowprice':
                low_output_photo(bot=bot, message=message)
            elif command == '/bestdeal':
                msg = bot.send_message(message.chat.id, '<b>Введите минимальную цену за номер</b>')
                bot.register_next_step_handler(msg, min_price)
    else:
        bot.send_message(message.chat.id, '<b>Введите количество фотографий цифрами.</b>')
        bot.register_next_step_handler(message, get_photo)
