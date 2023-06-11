from database import *
from telebot.types import Message
from utils.misc.user import get_user
from keyboards.inline.yes_no_photo import photo_answer
from loader import bot
from database.SQLite_database import *


def hotel_numbers(message: Message):
    if message.text.isdigit():
        if int(message.text) > 10:
            message.text = '10'
            with database:
                user = get_user(message)
                user.hotels_num = message.text
                user.save()
            bot.send_message(message.chat.id, f'<b>Максимальное количество отелей 10. '
                                              f'Будет показано {message.text} отелей.\nПоказывать фотографии?</b>',
                             reply_markup=photo_answer())
        else:
            with database:
                user = get_user(message)
                user.hotels_num = message.text
                user.save()
            bot.send_message(message.chat.id, f'<b>Будет показано {message.text} отелей.\nПоказывать фотографии?</b>',
                             reply_markup=photo_answer())
    else:
        bot.send_message(message.chat.id, '<b>Введите количество отелей цифрами.</b>')
        bot.register_next_step_handler(message, hotel_numbers)
