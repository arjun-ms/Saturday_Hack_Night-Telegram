import os
import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from PIL import Image
import shutil
from time import sleep
import fitz

API_TOKEN = "2028672930:AAFcByU0eZcAwoD3VCMp3ESflj_zjd6b7cE"
bot = telebot.TeleBot(API_TOKEN, parse_mode="Markdown")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    try:
        bot.send_chat_action(message.chat.id, "typing")
        strtMsg = f'''
		Hey [{message.from_user.first_name} {message.from_user.last_name}](tg://user?id={message.chat.id})! This bot will helps you to do many things with pdf's 🥳
		Some of the main features are:
		◍ Convert images to PDF
		'''
        key = types.InlineKeyboardMarkup()
        key.add(types.InlineKeyboardButton("Source Code ❤️", callback_data="strtDevEdt"),
                types.InlineKeyboardButton("Explore More 🔍", callback_data="imgsToPdfEdit"))
        bot.send_message(message.chat.id, strtMsg,
                         disable_web_page_preview=True, reply_markup=key)

    except:
        pass

@bot.callback_query_handler(func=lambda call: call.data)
def strtMsgEdt(call):
	edit = call.data
	
	if edit == 'strtDevEdt':
		
		try:
			aboutDev = f'''About:
			Lang Used: Python🐍
			[Source Code](https://github.com/arjun-ms/Saturday_Hack_Night-Telegram/tree/main/Code_Buddies)
			if you ❤ this, Star this repo
			'''
			key = types.InlineKeyboardMarkup()
			key.add(types.InlineKeyboardButton("🔙 Home 🏡", callback_data="back"))
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = aboutDev, disable_web_page_preview=True, reply_markup=key)
		
		except:
			pass
		
	elif edit == 'imgsToPdfEdit':
		
		try:
			expMsg = f'''
		Images to pdf :
		Just Send/forward me some images. When you are finished; use /generate to get your pdf..😉

		 ◍ Image Sequence will be considered 🤓
		 ◍ For better quality pdfs(send images without Compression) 🤧
 
		 ◍ `/cancel` - Delete's the current Queue 😒
		 ◍ `/id` - to get your telegram ID 🤫
 
		 ◍ RENAME YOUR PDF:
			- By default, your telegram ID will be treated as your pdf name..🙂
			- `/generate fileName` - to change pdf name to fileName🤞
			- `/generate name` - to get pdf with your telegram name
		'''
			key = types.InlineKeyboardMarkup()
			key.add(types.InlineKeyboardButton("🔙 Home 🏡", callback_data="back"),types.InlineKeyboardButton("PDF to images ➡️", callback_data="pdfToImgsEdit"))
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = expMsg, disable_web_page_preview=True, reply_markup=key)
		
		except:
			pass
		
	elif edit == 'pdfToImgsEdit':
		
		try:
			expMsg = f'''
        PDF to images:

		Just Send/forward me a pdf file.

 		◍ I will Convert it to images ✌️
 		◍ if Multiple pages in pdf(send as albums) 😌
 		◍ Page numbers are sequentially ordered 😬

		⚠️ Due to overload this bot will only convert files less than 10mb files..⚠️

		if you need to convert 10mb+ you can create your own bot.. Source code is mentioned in bio 😇
		'''
			key = types.InlineKeyboardMarkup()
			key.add(types.InlineKeyboardButton("🔙 Imgs To Pdf", callback_data="imgsToPdfEdit"),types.InlineKeyboardButton("Home 🏡", callback_data="back"),types.InlineKeyboardButton("Warning ⚠", callback_data="warningEdit"))
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = expMsg, disable_web_page_preview=True, reply_markup=key)
		
		except:
			pass
		
	
	elif edit == 'warningEdit':
		
		try:
			expMsg = f'''
			WARNING MESSAGE ⚠️:

			◍ This bot is completely free to use so please dont spam here 🙏

			◍ Please don't try to spread 18+ contents 😒

			'''
			key = types.InlineKeyboardMarkup()
			key.add(types.InlineKeyboardButton("🔙 Back", callback_data="pdfToImgsEdit"),types.InlineKeyboardButton("Home 🏡", callback_data="back"))
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = expMsg, disable_web_page_preview=True, reply_markup=key)
		
		except:
			pass
		
	elif edit == 'back':
		
		try:
			strtMsg = f'''
		Hey..!! This bot will helps you to do many things with pdf's 🥳

		Some of the main features are:
		◍ `Convert images to PDF`
		◍ `Convert PDF to images`
		'''
			key = types.InlineKeyboardMarkup()
			key.add(types.InlineKeyboardButton("Source Code ❤️", callback_data="strtDevEdt"),types.InlineKeyboardButton("Explore More 🥳", callback_data="imgsToPdfEdit"))
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = strtMsg, disable_web_page_preview=True, reply_markup=key)
		
		except:
			pass
		
	elif edit == 'close':
		
		try:
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			
		except:
			pass


@bot.message_handler(commands=["id"])
def UsrId(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, f'Your ID - `{message.chat.id}`')


@bot.message_handler(commands=["help"])
def hlp(message):
    try:
        bot.send_chat_action(message.chat.id, "typing")
        hlpMsg = f'''
Help message:

 ◍ Hit on /start to get the welcome message

 ◍ Then Use `Explore more 🥳` button for more help

'''
        key = types.InlineKeyboardMarkup()
        key.add(types.InlineKeyboardButton("Close ⌛", callback_data="close"))
        bot.send_message(message.chat.id, hlpMsg,
                         disable_web_page_preview=True, reply_markup=key)

    except:
        pass


bot.polling()
