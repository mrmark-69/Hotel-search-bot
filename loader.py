import telebot
from config_data.config import BOT_TOKEN

bot = telebot.TeleBot(token=BOT_TOKEN, parse_mode='html', colorful_logs=True)
