from utils.misc.user import get_user
from loader import bot
from all_requests.region import get_region_id
from keyboards.inline.locations import locations_keyboard
from utils.misc.target import send_target
from database.SQLite_database import *
from database.models import Location


@bot.callback_query_handler(
    func=lambda call: call.data in ['yes', 'no'])  # Обработчик событий на нажатие
# inline-кнопок "да" и "нет".
def get_callback_1(call):
    if call.data:
        if call.data == 'yes':
            with database:
                user = get_user(call.message)
                city = user.city
                locations = get_region_id(city)
                if locations:
                    for key, value in locations.items():
                        Location.create(user_id=user.user_id, region_id=key, location_name=value)
                    bot.send_message(call.message.chat.id, '<b>Ок, Уточните локацию.</b>',
                                     reply_markup=locations_keyboard(locations))
                else:
                    bot.send_message(call.message.chat.id,
                                     '<b>С таким названием ничего не найдено.\nВведите другой пункт назначения.</b>')
                    bot.register_next_step_handler(call.message, send_target)
        elif call.data == 'no':
            bot.send_message(call.message.chat.id, '<b>Введите пункт назначения.</b>')
            bot.register_next_step_handler(call.message, send_target)
