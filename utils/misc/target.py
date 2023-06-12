from telebot.types import Message
from all_requests.region import get_region_id
from database.models import Location
from keyboards.inline.locations import locations_keyboard
from utils.misc.user import get_user
from loader import bot
from database.SQLite_database import *


def send_target(message: Message):
    target = message.text
    with database:
        user = get_user(message)
        user.city = target
        user.save()
        locations = get_region_id(target)
        if locations:
            for key, value in locations.items():
                Location.create(user_id=user.user_id, region_id=key, location_name=value)
            bot.send_message(message.chat.id, '<b>Ок, Уточните локацию.</b>',
                             reply_markup=locations_keyboard(locations))
        else:
            bot.send_message(message.chat.id,
                             '<b>С таким названием ничего не найдено.\nВведите другой пункт назначения.</b>')
            bot.register_next_step_handler(message, send_target)
