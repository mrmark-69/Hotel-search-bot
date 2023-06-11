from telebot.types import InlineKeyboardMarkup
from telegram_bot_calendar import DetailedTelegramCalendar
from datetime import date


def calendar_out() -> InlineKeyboardMarkup:
    calendar, step = DetailedTelegramCalendar(calendar_id=1, locale='ru', min_date=date.today()).build()
    return calendar
