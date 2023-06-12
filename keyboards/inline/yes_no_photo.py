from telebot import types
from telebot.types import InlineKeyboardMarkup


def photo_answer() -> InlineKeyboardMarkup:
    """
       Клавиатура с кнопками "Да", "Нет"
       :return: клавиатура InlineKeyboardMarkup
       """
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(text='Да', callback_data='yes')
            ],
            [
                types.InlineKeyboardButton(text='Нет', callback_data='no')
            ]
        ]
    )
