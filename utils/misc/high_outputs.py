from utils.misc.user import get_user
from all_requests.hotels import get_hotels
from utils.misc.outputs import *
from utils.misc.history import make_history
from utils.misc.get_high import high_price
from database.SQLite_database import *


def high_output(bot, message):
    bot.send_message(message.chat.id, '<b>Выбрано - без фото.\nОк, Я ищу...</b>')
    with database:
        user = get_user(message)
        make_history(user)
        hotels = get_hotels(user.region_id, user.date_in, user.date_out, user.min_price, user.max_price)
        if hotels:
            high_hotels = high_price(number_of_hotels=user.hotels_num, hotels=hotels)
            selected = [hotel for i, hotel in enumerate(high_hotels) if i < user.hotels_num]
            output_without_photo(bot=bot, selected=selected, message=message)
        else:
            bot.send_message(message.chat.id,
                             '<b>Произошла ошибка, повторите поиск позже или с другими параметрами</b>')


def high_output_photo(bot, message):
    bot.send_message(message.chat.id, '<b>Ок, Я ищу...</b>')
    with database:
        user = get_user(message)
        make_history(user)
        hotels = get_hotels(user.region_id, user.date_in, user.date_out, user.min_price, user.max_price)
        if hotels:
            high_hotels = high_price(number_of_hotels=user.hotels_num, hotels=hotels)
            selected = [hotel for i, hotel in enumerate(high_hotels) if i < user.hotels_num]
            output_with_photos(bot=bot, selected=selected, message=message, user=user)
        else:
            bot.send_message(message.chat.id,
                             '<b>Произошла ошибка, повторите поиск позже или с другими параметрами</b>')
