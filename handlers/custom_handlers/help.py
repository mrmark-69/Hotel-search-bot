from telebot.types import Message
from loader import bot


@bot.message_handler(commands=['help'])
def get_help(message: Message):
    if message.text == '/help':
        bot.send_message(message.chat.id,
                         'Этот бот поможет вам найти отель.\n'
                         'Для начала работы нажмите кнопку меню и выберите старт /start\n'
                         'Есть несколько категорий поиска:\n'
                         '/highprice - ищет отели в порядке убывания цены, начиная с дорогих.\n'
                         '/lowprice - ищет отели в порядке возрастания цены.\n'
                         '/bestdeal - позволяет задать цену отеля и расстояние от центра.\n'
                         '/history - выведет историю запросов.')
