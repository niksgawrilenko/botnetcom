import telebot
import datetime
import pprint
import random
from pymongo import MongoClient
from telebot import types

cluster = MongoClient('mongodb+srv://nikitosik:Nikita_gawrilenko2002@cluster0.5c8tu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster.myFirstDatabase
collection =db.users
# test=collection.find_one({"email":"nikitagawrilenko20222219@gmail.com"})
# print(test)
#nikitosik:Nikita_gawrilenko2002
bot = telebot.TeleBot('5126706421:AAFWyve-bLWA15yG4lqRPoKpeLwyV1wkenM')
email= ''

@bot.message_handler(commands=["start"])
def start(message, res=False):
    textMess='Привет! Я чат-бот компании NetCom, ваш виртуальный помощник! Я не живой человек, но могу быстро найти ответ на любой вопрос о услугах NetCom.Уточните, ви являетеся абонентом нашей компании(Да/Нет)?'
    bot.send_message(message.from_user.id, textMess)

@bot.message_handler(content_types=["text"])
def client(message):
    if message.text == "Да":
        bot.register_next_step_handler(message, email)
    elif message.text == "Нет" :
        textMess="Желаете узнать или подключить наши услуги? Посетите наш сайт и подайте заявку! https://nikitosiknetcom.000webhostapp.com/signup.php"
        bot.send_message(message.from_user.id, textMess)
        bot.register_next_step_handler(message, client)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши снова ")
        bot.register_next_step_handler(message, start)

def email(message):
    bot.send_message(message.from_user.id, "Введите ваш электронный адрес")
    bot.register_next_step_handler(message, avtorisation)
def avtorisation(message):
    email = message.text
    user_dict =collection.find_one({"email":email})
    bot.send_message(message.from_user.id,"Привет, " +str(user_dict['username'])+ ", Твой баланс:  "+str(user_dict['balans'])+' грн.')
    bot.register_next_step_handler(message, direct)

def direct(message):
    print(message.text)


bot.infinity_polling()