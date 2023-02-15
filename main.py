import os
import telebot
import sqlite3
from dotenv import load_dotenv
from telebot import types

load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(id INTEGER)""")
    connect.commit()

    user_id = [message.chat.id]
    cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
    connect.commit()


@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.chat.id,"https://habr.com/ru/users/lubaznatel/")

bot.polling()