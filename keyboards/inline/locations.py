from typing import Dict
from telebot import types
from telebot.types import InlineKeyboardMarkup


def locations_keyboard(locations: Dict) -> InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        [[types.InlineKeyboardButton(text=value, callback_data=key)] for key, value in locations.items()])
