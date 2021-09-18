import os
from dotenv import load_dotenv
load_dotenv()
import telebot
from telebot import types,util

bot = telebot.TeleBot(os.environ.get("API_KEY"))
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if(message.text.lower() in ["hi","hello","start"]):
		bot.reply_to(message, "Hello 👋")

bot.polling()