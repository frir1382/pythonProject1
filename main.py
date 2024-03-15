import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '6484963335:AAEIeOxtZ9Q1FSF7POjDJJwem29k7_g4JWk'
URL = 'https://cataas.com/cat'

bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True)
keyboard.add(KeyboardButton('Котика!'))
keyboard.add(KeyboardButton('Об авторе'))
def get_cat():
    response = requests.get(URL)
    return response.content


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Я бот созданный для котов и радости!",
                     reply_markup=keyboard)

@bot.message_handler(regexp='кот')
def cat_image_message(message):
    photo = get_cat()
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(func=lambda s: 'Об авторе' in s.text)
def echo_message(message):
    bot.send_message(message.chat.id, "Я Сериков Константин создал этот бот чтобы получить зачот по проекту.")


bot.infinity_polling()




#6484963335:AAEIeOxtZ9Q1FSF7POjDJJwem29k7_g4JWk'


