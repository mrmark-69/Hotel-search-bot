from utils.misc.user import get_user
from loader import bot
import re
from keyboards.calendar.calendar_enter import calendar_in
from database.SQLite_database import *
from database.models import Location


@bot.callback_query_handler(func=lambda call: True)  # Обработчик событий на нажатие всех inline-кнопок
def get_callback(call):
    if call.data:  # проверяем есть ли данные если да, проверяем на соответствие шаблону.
        if re.search(r'\d+$', call.data):  # Фильтр для пропуска id локации
            with database:
                user = get_user(call.message)
                user.region_id = call.data  # id локации
                location = Location.get(Location.region_id == user.region_id)
                user.location = location.location_name
                user.save()
            bot.send_message(call.message.chat.id, f'<b>Вы выбрали локацию:\n{user.location}\n</b>'
                                                   f'<b>Выберите дату заезда.</b>',
                             reply_markup=calendar_in())
