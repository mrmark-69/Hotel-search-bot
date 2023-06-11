from telegram_bot_calendar import DetailedTelegramCalendar
from loader import bot
from utils.misc.user import get_user
from datetime import date
from database.SQLite_database import *
from keyboards.calendar.calendar_exit import calendar_out

RUSTEP = {'y': 'год', 'm': 'месяц', 'd': 'день'}


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=0))
def cal_in(call):
    result, key, step = DetailedTelegramCalendar(calendar_id=0, locale='ru', min_date=date.today()).process(call.data)
    if not result and key:
        bot.edit_message_text(f"Выберите {RUSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        with database:
            user = get_user(call.message)
            user.date_in = result
            user.save()
        bot.edit_message_text(f"<b>Дата заезда: {result}</b>",
                              call.message.chat.id,
                              call.message.message_id)
        bot.send_message(call.message.chat.id,
                         f'<b>Выберите дату отъезда.</b>',
                         reply_markup=calendar_out())
