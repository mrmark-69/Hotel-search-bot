from utils.misc.user import get_user
from all_requests.hotels import get_hotels
from utils.misc.outputs import *
from utils.misc.history import make_history
from utils.misc.destination import destination
from database.SQLite_database import *


def distance_output(bot, message):
    bot.send_message(message.chat.id, '<b>Выбрано - без фото.\nОк, Я ищу...</b>')
    with database:
        user = get_user(message)
        make_history(user)
        hotels = get_hotels(user.region_id, user.date_in, user.date_out, user.min_price, user.max_price)
        if hotels:
            dist_hotels = destination(hotels=hotels)
            selected = [hotel for i, hotel in enumerate(dist_hotels) if
                        i < user.hotels_num & user.distance >= hotel['distance_from']]
            if len(selected) > 0:
                output_without_photo(bot=bot, selected=selected, message=message)
            else:
                bot.send_message(message.chat.id,
                                 '<b>В пределах заданного расстояния от центра ничего подходящего не найдено.</b>')
        else:
            bot.send_message(message.chat.id,
                             '<b>Произошла ошибка, повторите поиск позже или с другими параметрами</b>')


def distance_output_photo(bot, message):
    bot.send_message(message.chat.id, '<b>Ок, Я ищу...</b>')
    with database:
        user = get_user(message)
        make_history(user)
        hotels = get_hotels(user.region_id, user.date_in, user.date_out, user.min_price, user.max_price)
        if hotels:
            dist_hotels = destination(hotels=hotels)
            selected = [hotel for i, hotel in enumerate(dist_hotels) if
                        i < user.hotels_num & user.distance >= hotel['distance_from']]
            if len(selected) > 0:
                output_with_photos(bot=bot, selected=selected, message=message, user=user)
            else:
                bot.send_message(message.chat.id,
                                 '<b>В пределах заданного расстояния от центра ничего подходящего не найдено.</b>')
        else:
            bot.send_message(message.chat.id,
                             '<b>Произошла ошибка, повторите поиск позже или с другими параметрами</b>')
