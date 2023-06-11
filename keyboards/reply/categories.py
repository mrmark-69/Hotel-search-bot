from telebot import types
from telebot.types import ReplyKeyboardMarkup


def search_category() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    high = types.KeyboardButton('/highprice')
    low = types.KeyboardButton('/lowprice')
    best_deal = types.KeyboardButton('/bestdeal')
    history = types.KeyboardButton('/history')
    keyboard.add(high, low, best_deal, history)
    return keyboard
