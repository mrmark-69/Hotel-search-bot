from telebot.types import Message
from keyboards.reply.categories import search_category
from loader import bot
from database.SQLite_database import *
from database.models import Location
from database.models.user import User


@bot.message_handler(commands=['start'])
def start(message: Message):
    if message.text == '/start':
        with database:
            user_to_delete = User.get_or_none(user_id=message.chat.id)
            locations_to_delete = Location.get_or_none(user_id=message.chat.id)
            if user_to_delete:
                user_to_delete.delete_instance()
            if locations_to_delete:
                Location.delete().where(Location.user_id == message.chat.id).execute()
            User.create(user_id=message.chat.id)
        bot.send_message(message.chat.id,
                         f'<b>Здравствуйте {message.from_user.full_name}! Я бот, который поможет Вам найти отель. '
                         'Выберите категорию поиска.</b>', reply_markup=search_category())
