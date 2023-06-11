from utils.misc.user import get_user
from all_requests.hotels import get_hotels
from utils.misc.outputs import *
from utils.misc.history import make_history
from database.SQLite_database import *


def low_output(bot, message):
    bot.send_message(message.chat.id, '<b>Выбрано - без фото.\nОк, Я ищу...</b>')
    with database:
        user = get_user(message)
        make_history(user)
        hotels = get_hotels(user.region_id, user.date_in, user.date_out, user.min_price, user.max_price)
        if hotels:
            selected = [hotel for i, hotel in enumerate(hotels) if i < user.hotels_num]
            output_without_photo(bot=bot, selected=selected, message=message)
        else:
            bot.send_message(message.chat.id,
                             '<b>Произошла ошибка, повторите поиск позже или с другими параметрами</b>')


def low_output_photo(bot, message):
    bot.send_message(message.chat.id, '<b>Ок, Я ищу...</b>')
    with database:
        user = get_user(message)
        make_history(user)
        hotels = get_hotels(user.region_id, user.date_in, user.date_out, user.min_price, user.max_price)
        if hotels:
            selected = [hotel for i, hotel in enumerate(hotels) if i < user.hotels_num]
            output_with_photos(bot=bot, selected=selected, message=message, user=user)
        else:
            bot.send_message(message.chat.id,
                             '<b>Произошла ошибка, повторите поиск позже или с другими параметрами</b>')
