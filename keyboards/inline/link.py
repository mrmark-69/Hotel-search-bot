from telebot import types
from telebot.types import InlineKeyboardMarkup, WebAppInfo


def get_site(hotel_id: str) -> InlineKeyboardMarkup:
    """
    Функция для ин-лайн-кнопки, которая открывает страницу отеля на Hotels.com в окне телеграм.
    :return: InlineKeyboardButton
    """
    key_board = types.InlineKeyboardMarkup()
    # Параметр web_app=WebAppInfo(url='https://www....') позволяет при нажатии кнопки открывать сайт
    # прямо в окне телеграм
    key_board.add(types.InlineKeyboardButton('Открыть страницу отеля на Hotels.com', web_app=WebAppInfo(
        url=f'https://www.hotels.com/h{hotel_id}.Hotel-Information')))
    return key_board
