from telegram_bot_calendar import DetailedTelegramCalendar
from loader import bot
from utils.misc.user import get_user
from utils.misc.hotels_num import hotel_numbers
from database.SQLite_database import *

RUSTEP = {'y': 'год', 'm': 'месяц', 'd': 'день'}


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
def cal_out(call):
    with database:
        user = get_user(call.message)
        min_date = user.date_in
    result, key, step = DetailedTelegramCalendar(calendar_id=1, locale='ru', min_date=min_date).process(call.data)
    if not result and key:
        bot.edit_message_text(f"Выберите {RUSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        with database:
            user = get_user(call.message)
            user.date_out = result
            user.save()
        bot.edit_message_text(f"<b>Дата выезда: {result}</b>",
                              call.message.chat.id,
                              call.message.message_id)
        msg = bot.send_message(call.message.chat.id,
                               '<b>Сколько отелей искать?</b>(не более 10)')
        bot.register_next_step_handler(msg, hotel_numbers)
