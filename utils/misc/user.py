from telebot.types import Message
from database.models.user import User


def get_user(message: Message):
    user = User.get(User.user_id == message.chat.id)
    return user
