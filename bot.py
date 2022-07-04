# -*- coding: utf-8 -*-
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#             ...

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'''Я пробил инфрмацию:
                                      
id чата: {message.chat.id}
id пользователя: {message.from_user.id}
имя: {message.from_user.first_name}
фамилия: {message.from_user.last_name}
псевдоним: {message.from_user.username}
                                      
текст сообщения: {message.text}''')


bot.polling()
