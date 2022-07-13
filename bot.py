# -*- coding: utf-8 -*-
import telebot
import os
from telebot import types
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from random import *
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


def pidr():
    x = choice([1, 2, 3, 4, 5, 6, 7])
    if x == 1:
        file1 = open("Я.png", 'rb')
        y = ("Игорь", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[1]) + 1)
            s0.pop(1)
            s0.insert(1, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!!! Пидарасом дня 
{datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 
Вызвать орловского помощника: /orel''')

    if x == 2:
        file1 = open("Филч.png", 'rb')
        y = ("Филч", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[0]) + 1)
            s0.pop(0)
            s0.insert(0, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!!! Пидарасом дня 
{datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 
Вызвать орловского помощника: /orel''')

    if x == 3:
        file1 = open("Серега.png", 'rb')
        y = ("Серега", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[2]) + 1)
            s0.pop(2)
            s0.insert(2, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!! Пидарасом дня 
{datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 
Вызвать орловского помощника: /orel''')

    if x == 4:
        file1 = open("Леха.png", 'rb')
        y = ("Леха(Саня)", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[4]) + 1)
            s0.pop(4)
            s0.insert(4, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!! Пидарасом дня 
{datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 
Вызвать орловского помощника: /orel''')

    if x == 5:
        file1 = open("фитиль.jpg", 'rb')
        y = ("Леха(Фитиль)", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[5]) + 1)
            s0.pop(5)
            s0.insert(5, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!! Пидарасом дня 
{datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 
Вызвать орловского помощника: /orel''')

    if x == 6:
        file1 = open("маугли.png", 'rb')
        y = ("Маугли", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[6]) + 1)
            s0.pop(6)
            s0.insert(6, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!! Пидарасом дня 
{datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 
Вызвать орловского помощника: /orel''')

    if x == 7:
        file1 = open("саня.png", 'rb')
        y = ("Саня", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[3]) + 1)
            s0.pop(3)
            s0.insert(3, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!! Пидарасом дня 
{datetime.now().day, datetime.now().month, datetime.now().year} объявляется {y[0]} 
Вызвать орловского помощника: /orel''')


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    if callback.data == 'btn':
        file2 = open("важно.png", 'rb')
        bot.send_photo('@suetologyorla', file2)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message('@suetologyorla', ('Основные команды поддерживаемые ботом:\n'
                                        '/orel -  вызвать орловского помощника\n'
                                        '/pidorstat - пидорский рейтинг \n'
                                        '/start - инициализация бота\n'
                                        '/help - справка по боту\n'
                                        '/test - тестирование бота'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message('@suetologyorla', '''Бот уже инициализирован.
Я работаю по расписанию. Пидр дня назначается ежедневно 
в 14:00 по московскому времени

/help - справка по боту''')


def pstat():
    stat_file = open("статистика", 'r+')
    d0 = stat_file.read().split(sep='\n')
    d1 = [(int(d0[0]), "Филч"), (int(d0[1]), "Игорь"), (int(d0[2]), "Серега"), (int(d0[3]), "Саня"),
          (int(d0[4]), "Леха(Саня)"), (int(d0[5]), "Леха(Фитиль)"), (int(d0[6]), "Диман")]
    d1_sort = sorted(d1, reverse=True)
    stat_file.close()
    return (f'''РЕЙТИНГ ПИДАРАСОВ:

1. {d1_sort[0][1]} -----> {d1_sort[0][0]} раз(а)
2. {d1_sort[1][1]} -----> {d1_sort[1][0]} раз(а)
3. {d1_sort[2][1]} -----> {d1_sort[2][0]} раз(а)
4. {d1_sort[3][1]} -----> {d1_sort[3][0]} раз(а)
5. {d1_sort[4][1]} -----> {d1_sort[4][0]} раз(а)
6. {d1_sort[5][1]} -----> {d1_sort[5][0]} раз(а)
7. {d1_sort[6][1]} -----> {d1_sort[6][0]} раз(а)

Да здравствует наш чемпион {d1_sort[0][1]}! Его результативности 
может позавидовать Элтон Джон и другие Великие. Пожелаем
ему здоровья, успехов в личной жизни и новыйх побед.

/help - справка по боту''')


@bot.message_handler(commands=['pidorstat'])
def test(message):
    bot.send_message('@suetologyorla', pstat())


@bot.message_handler(commands=['test'])
def start(message):
    bot.send_message('@suetologyorla', '''Протестируй себя петушок...А моя работа давно проверена и отлажена.

/help - справка по боту''')


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(pidr, 'interval', seconds=30)
    scheduler.start()

    try:
        @bot.message_handler(commands=['orel'])
        def orel(message):
            bot.send_message('@suetologyorla', 'Орловский помощник..', reply_markup=kb1)
    except KeyboardInterrupt:
        pass

bot.polling()
