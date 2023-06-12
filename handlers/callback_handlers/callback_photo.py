from utils.misc.user import get_user
from loader import bot
from utils.misc.photo import get_photo
from utils.misc.high_outputs import high_output
from utils.misc.low_outputs import low_output
from utils.misc.price import min_price
from database.SQLite_database import *


@bot.callback_query_handler(
    func=lambda call: call.data in ['yes', 'no'])  # Обработчик событий на нажатие
# inline-кнопок "да" и "нет".
def get_callback_2(call):
    if call.data:
        if call.data == 'yes':
            bot.send_message(call.message.chat.id, '<b>Введите количество фото.</b>(не более 10)')
            bot.register_next_step_handler(call.message, get_photo)
        elif call.data == 'no':
            with database:
                user = get_user(call.message)
                user.photo_num = 0
                command = user.command
                user.save()
            if command == '/highprice':
                high_output(bot=bot, message=call.message)
            elif command == '/lowprice':
                low_output(bot=bot, message=call.message)
            elif command == '/bestdeal':
                bot.send_message(call.message.chat.id, '<b>Выбрано - без фото.\n'
                                                       'Введите минимальную цену за номер</b>')
                bot.register_next_step_handler(call.message, min_price)
