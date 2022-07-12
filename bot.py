# -*- coding: utf-8 -*-
import telebot
import os
from telebot import types
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from random import *

token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token)

kb1 = types.InlineKeyboardMarkup(row_width=1)
but1 = types.InlineKeyboardButton(text='Купить билет в Орёл',
                                  url='https://жд-билеты.сайт/kupit-zhd-bilety/#/moskva/orel?')
but2 = types.InlineKeyboardButton(text='Бронь стола на Привале', url='http://onmap.uz/tel/74862484006')
but3 = types.InlineKeyboardButton(text='Бронь стола 7 пятниц', url='http://onmap.uz/tel/74862490008')
but4 = types.InlineKeyboardButton(text='Бронь стола Шаривари', url='http://onmap.uz/tel/74862445303')
but5 = types.InlineKeyboardButton(text='Важное про Орёл', callback_data='btn')
kb1.add(but1, but2, but3, but4, but5)

stat_fil = 1
stat_serg = 2
stat_igor = 0
stat_sanya = 0
stat_leha = 0
stat_fitil = 0
stat_maugli = 0


def stat(stat_fil, stat_serg, stat_igor, stat_sanya, stat_leha, stat_fitil, stat_maugli):
    d1 = {"Филч": stat_fil, "Игорь": stat_igor, "Серега": stat_serg, "Саня": stat_sanya, "Леха(Саня)": stat_leha,
          "Леха(Фитиль)": stat_fitil, "Диман": stat_maugli}
    d1_sort = sorted(d1.items(), reverse=True)
    return d1_sort


def pidr(stat_fil, stat_serg, stat_igor, stat_sanya, stat_leha, stat_fitil, stat_maugli):
    x = choice([1, 2, 3, 4, 5, 6, 7])
    if x == 1:
        file1 = open("Я.png", 'rb')
        y = ("Игорь", file1)
        stat_igor += 1
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!!! Пидарасом дня 
        {datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')
    if x == 2:
        file1 = open("Филч.png", 'rb')
        y = ("Филч", file1)
        stat_fil += 1
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!!! Пидарасом дня 
        {datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')
    if x == 3:
        file1 = open("Серега.png", 'rb')
        y = ("Серега", file1)
        stat_serg += 1
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!! Пидарасом дня 
        {datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')
    if x == 4:
        file1 = open("Леха.png", 'rb')
        y = ("Леха(Саня)", file1)
        stat_leha += 1
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!! Пидарасом дня 
        {datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')
    if x == 5:
        file1 = open("фитиль.jpg", 'rb')
        y = ("Леха(Фитиль)", file1)
        stat_fitil += 1
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!! Пидарасом дня 
        {datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')
    if x == 6:
        file1 = open("маугли.png", 'rb')
        y = ("Маугли", file1)
        stat_maugli += 1
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!! Пидарасом дня 
        {datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 


                                                                            Вызвать орловского помощника: /orel''')
    if x == 7:
        file1 = open("саня.png", 'rb')
        y = ("Саня", file1)
        stat_sanya += 1
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!! Пидарасом дня 
        {datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    if callback.data == 'btn':
        file2 = open("важно.png", 'rb')
        bot.send_photo('@hloappstest', file2)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message('@hloappstest', '''Основные команды поддерживаемые ботом:
/orel -  вызвать орловского помощника
/pidorstat - пидорский рейтинг 
/start - инициализация бота
/help - справка по боту
/test - тестирование бота''')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message('@hloappstest', '''Бот уже инициализирован.
Я работаю по расписанию. Пидр дня назначается ежедневно 
в 14:00 по московскому времени

/help - справка по боту''')


@bot.message_handler(commands=['pidorstat'])
def test(message, d1_sort):
    bot.send_message('@hloappstest', f'''РЕЙТИНГ ПИДАРАСОВ:

1. {d1_sort[0][0]} -----> {d1_sort[0][1]} раз(а)
2. {d1_sort[1][0]} -----> {d1_sort[1][1]} раз(а)
3. {d1_sort[2][0]} -----> {d1_sort[2][1]} раз(а)
4. {d1_sort[3][0]} -----> {d1_sort[3][1]} раз(а)
5. {d1_sort[4][0]} -----> {d1_sort[4][1]} раз(а)
6. {d1_sort[5][0]} -----> {d1_sort[5][1]} раз(а)
7. {d1_sort[6][0]} -----> {d1_sort[6][1]} раз(а)

Да здравствует наш чемпион {d1_sort[0][0]}! Его результативности 
может позавидовать Элтон Джон и другие Великие. Пожелаем
ему здоровья, успехов в личной жизни и новыйх побед.

/help - справка по боту''')
    

@bot.message_handler(commands=['test'])
def start(message):
    bot.send_message('@hloappstest', '''Протестируй себя петушок...А моя работа давно проверена и отлажена.

/help - справка по боту''')


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(pidr, 'cron', day_of_week='mon-sun', hour=11)
    scheduler.start()

    try:
        @bot.message_handler(commands=['orel'])
        def orel(message):
            bot.send_message('@hloappstest', 'Орловский помощник..', reply_markup=kb1)
    except KeyboardInterrupt:
        pass


bot.polling()
