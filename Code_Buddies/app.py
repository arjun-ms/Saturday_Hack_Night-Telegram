import os
import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from PIL import Image
import shutil
from time import sleep
import fitz

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN, parse_mode="Markdown")

@bot.message_handler(commands=["start"])
def send_welcome(message):
	try:
		bot.send_chat_action(message.chat.id, "typing")
		strtMsg = f'''
Hey [{message.from_user.first_name}](tg://user?id={message.chat.id})..!! This bot will helps you to do many things with pdf's 🥳

Some of the main features are:
◍ `Convert images to PDF``
'''
		key = types.InlineKeyboardMarkup()
		key.add(types.InlineKeyboardButton("Source Code ❤️", callback_data="strtDevEdt"),types.InlineKeyboardButton("Explore More 🥳", callback_data="imgsToPdfEdit"))
		bot.send_message(message.chat.id, strtMsg, disable_web_page_preview=True, reply_markup=key)
	
	except:
		pass



@bot.callback_query_handler(func=lambda call: call.data)
def strtMsgEdt(call):
	edit = call.data
	
	if edit == 'strtDevEdt':
		
		try:
			key = types.InlineKeyboardMarkup()
			key.add(types.InlineKeyboardButton("Home 🏡", callback_data="back"))
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, disable_web_page_preview=True, reply_markup=key)
		
		except:
			pass
		
	elif edit == 'imgsToPdfEdit':
		
		try:
			expMsg = f'''
Images to pdf :

		Just Send/forward me some images. When you are finished; use /generate to get your pdf..

 ◍ Image Sequence will be considered 
 ◍ For better quality pdfs(send images without Compression) 
 
 ◍ `/cancel` - Delete's the current Queue 
 ◍ `/id` - to get your telegram ID 
 '''
			key = types.InlineKeyboardMarkup()
			key.add(types.InlineKeyboardButton("Home 🏡", callback_data="back"),types.InlineKeyboardButton("PDF to images ➡️", callback_data="pdfToImgsEdit"))
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = expMsg, disable_web_page_preview=True, reply_markup=key)
		
		except:
			pass