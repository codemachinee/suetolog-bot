# -*- coding: utf-8 -*-
import telebot
import gspread
import os
from telebot import types
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from random import *
from functions_file import value_plus_one, pstat, obnulenie_stat, ball_of_fate, Davinci, Artur, celebrate_day, \
    Artur_pozdravlyaet
from paswords import *

#token = lemonade
token = codemashine_test
#token = major_suetolog

bot = telebot.TeleBot(token)

kb1 = types.InlineKeyboardMarkup(row_width=1)
but1 = types.InlineKeyboardButton(text='Купить билет в Орёл',
                                  url='https://жд-билеты.сайт/kupit-zhd-bilety/#/moskva/orel?')
but2 = types.InlineKeyboardButton(text='Бронь стола на Привале', url='http://onmap.uz/tel/74862484006')
but3 = types.InlineKeyboardButton(text='Бронь стола 7 пятниц', url='http://onmap.uz/tel/74862490008')
but4 = types.InlineKeyboardButton(text='Бронь стола Шаривари', url='http://onmap.uz/tel/74862445303')
but5 = types.InlineKeyboardButton(text='Таблица расходов', url='https://docs.google.com/spreadsheets/d'
                                                               '/1OJVOVnfRygWLN_OIK3w7FuAh37z0eAio0AkTbF7nBf4/edit'
                                                               '#gid=431148771')
but6 = types.InlineKeyboardButton(text='Яндекс.Диск', url='https://disk.yandex.ru/client/disk/бот%20суетологов/суетологи')
but7 = types.InlineKeyboardButton(text='Важное про Орёл', callback_data='btn')
but8 = types.InlineKeyboardButton(text='Шар судьбы', callback_data='bof')
but9 = types.InlineKeyboardButton(text='Игровой чат', url='http://178.57.222.84/http://178.57.222.84/')
kb1.add(but1, but2, but3, but4, but5, but6, but7, but8, but9)


def pidr():
    obnulenie_stat(bot)
    x = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if x == 1:
        file1 = open("Я.jpg", 'rb')
        y = ("Игорь", file1)
        value_plus_one('A2')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!!! {celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 2:
        file1 = open("Филч.jpg", 'rb')
        y = ("Филч", file1)
        value_plus_one('A1')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!!! {celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 3:
        file1 = open("Серега.jpg", 'rb')
        y = ("Серега", file1)
        value_plus_one('A3')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! {celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 4:
        file1 = open("Леха.jpg", 'rb')
        y = ("Леха(Саня)", file1)
        value_plus_one('A5')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! {celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 5:
        file1 = open("фитиль.jpg", 'rb')
        y = ("Леха(Фитиль)", file1)
        value_plus_one('A6')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! {celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 6:
        file1 = open("маугли.jpg", 'rb')
        y = ("Маугли", file1)
        value_plus_one('A7')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! {celebrate_day()}
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 7:
        file1 = open("саня.jpg", 'rb')
        y = ("Саня", file1)
        value_plus_one('A4')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! {celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 8:
        file1 = open("Кирилл.jpg", 'rb')
        y = ("Кирюха подкастер", file1)
        value_plus_one('A8')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! {celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 9:
        file1 = open("Женек.jpg", 'rb')
        y = ("Женек спасатель", file1)
        value_plus_one('A9')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! {celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()
    if x == 10:
        file1 = open("Евгений.png", 'rb')
        y = ("Женек старый", file1)
        value_plus_one('A10')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! {celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()
        
        
def dr():
    if datetime.now().day == 6 and datetime.now().month == 3:
        bot.send_message(group_id, Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения в сатирической форме Кириху '
                                                                f'Подкастера - Великого венчестера нашего коллектива. '
                                    f'Благодаря его стараниям и материалам мы в подробностях '
                                    f'восстанавливаем в памяти все что происходило не смотря на количество и качество '
                                    f'выпитого. Кирилл учится на юриста и до сих пор любит свою бывшую девушку'
                                    f'Лизу, но всячески это отрицает. Всегда вписывается в любое приключение, особенно '
                                    f'если это бесплатно. Прогуливает учебу в ресторанах KFC.'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 20 and datetime.now().month == 4:
        bot.send_message(group_id, Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения в сатирической форме Игоря, '
                                                                f'который поселил тебя в этом чате, '
                                                                f'а также беспалевно наполнил его своими родственниками.'
                                                                f'Игорь спортсмен и красавчик, парень который мечтал '
                                                                f'увидеть и покорить этот мир, но вместо этого сначала '
                                                                f'пошел в армию а потом еще и женился чтобы мечты '
                                                                f'навсегда остались недосигаемыми.'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 27 and datetime.now().month == 4:
        bot.send_message(group_id, Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения в сатирической форме Леху '
                                                                f'Фитиля. Этот парень настолько легендарный, что его '
                                                                f'видно издалека. '
                                          f'Многие девушки/женщины могут делать ему миньет не вставая на колени, но они'
                                          f' его давно не интересуют.. Леха любит бегать, ходить в баню, а после этого'
                                                                f'всего посещать макдоналдс. Леха душа компании и '
                                                                f'человек - настроение, Амбассадор шуток про геев и '
                                                                f'российских железных дорог.'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 5 and datetime.now().month == 5:
        bot.send_message(group_id, Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения в сатирической форме Илюху '
                                                                f'обладателя фамилии на которую бронируются все столики '
                                                                f'заведений города Орел. Илюха каратист, оптимист и '
                                                                f'хороший друг. Если Илюха перепивает, то он словно '
                                                                f'уходящая умирать в одиночестве кошка,  куда то скрывается '
                                                                f'чтобы поблевать. Илья водит Форд Фокус и живет в '
                                                                f'закрытом городе, любит томатное пиво.'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 19 and datetime.now().month == 5:
        bot.send_message(group_id, Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения в сатирической форме Женька '
                                                                f'Спасателя. Женек учится на спасателя, обладает пышными'
                                                                f'волосами, большим опытом работы официантом. Женек '
                                                                f'спит, только когда за рулем и везет пацанов в город '
                                                                f'Орел, в остальное время он либо работает либо пьет. '
                                                                f'Детство провел на Жилике и выжил там с женской '
                                                                f'прической'))
    elif datetime.now().day == 15 and datetime.now().month == 6:
        bot.send_message(group_id, Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения в сатирической форме Евгения'
                                                                f'Старого. Евгений самый старый обитатель чата, '
                                                                f'бизнесмен, владелец барбершопов в '
                                                                f'городе Москва, который любит активный образ жизни, '
                                                                f'кататься на сноуборде, плавать на байдарках, играть '
                                                                f'в сквош, а еще обожает шутки про геев, готовить '
                                                                f'алкогольные коктейли и путешествовать'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 14 and datetime.now().month == 7:
        bot.send_message(group_id, Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения в сатирической форме Димана,'
                                                                f'Диман копия Маугли из сказки Киплинга. '
                                                                f'Диман скрытый обитатель каменных джунглей, знает толк '
                                                                f'в кальянах и кальянщиках. Диман один из немногих в '
                                                                f'нашем чате кто уже стал отцом, однако умнее и '
                                                                f'серьезнее он от этого не стал!'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 16 and datetime.now().month == 7:
        bot.send_message(group_id, Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения в сатирической форме Серегу, '
                                                                f'который часто пропадает, но ярко появляется. Серега'
                                                                f'спортсмен, инвестор и тусовщик. Серега помимо того, '
                                                                f'что на ровне со всеми пьет, потом садится за '
                                                                f'руль и развозит их домой. Серега компанейский парень '
                                                                f'и душа компании.'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 8 and datetime.now().month == 9:
        bot.send_message(group_id, Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения в сатирической форме Саню, '
                                                                f'самого младшего обитателя нашего сообщества, который '
                                                                f'мог бы качественно использовать опыт старших товарищей, '
                                                                f'но использовать особо нечего. Саня в душе брокер '
                                                                f'который нагнул мир, но зачем то пошел учиться на '
                                                                f'военного и пока нагнул лишь только свои амбиции. Саня '
                                                                f'стильный, думает что мощный. Саня любит активный '
                                                                f'отдых, сноуборд, теннис, вейкборд и женщин. Саня '
                                                                f'пытается использовать '
                                                                f'свободу по полному но она ограничена отпуском'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 17 and datetime.now().month == 11:
        bot.send_message(group_id, Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения в сатирической форме Леха(Саня)'
                                                                f'Леха это стиль и харизма Востока. Леха любит когда все '
                                                                f'в этой жизни не дольше 4 минут. Леха любит все что '
                                                                f'горит и дымит. Леха заботливо следит чтобы все '
                                                                f'напились как следует и очень расстраивается если кто'
                                                                f'то не пьет. Леха бывший успешный тиктокер и школьный '
                                                                f'диджей!'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')

    elif datetime.now().day == 31 and datetime.now().month == 12:
        bot.send_message(group_id, f'🚨🚨🚨Внимание!🚨🚨🚨 Пидр Клаус подводит итоги...\n'
                                   f'Кто же станет пидаром года?')
        file = open('gif_mr.Bin.mp4', 'rb')
        bot.send_animation(group_id, file)
        gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
        sh = gc.open("bot_statistic")
        worksheet = sh.get_worksheet(0)
        d1 = [(int(worksheet.acell('C1').value), "Филч"), (int(worksheet.acell('C2').value), "Игорь"),
              (int(worksheet.acell('C3').value), "Серега"), (int(worksheet.acell('C4').value), "Саня"),
              (int(worksheet.acell('C5').value), "Леха(Саня)"), (int(worksheet.acell('C6').value), "Леха(Фитиль)"),
              (int(worksheet.acell('C7').value), "Диман"), (int(worksheet.acell('C8').value), "Кирюха подкастер"),
              (int(worksheet.acell('C9').value), "Женек спасатель"), (int(worksheet.acell('C10').value), "Женек старый")]
        d1_sort = sorted(d1, reverse=True)
        cell = worksheet.find(d1_sort[0][1], in_column=2)
        worksheet.update(f'D{cell.row}', f'{int(worksheet.acell(f"D{cell.row}").value) + 1}')
        bot.send_message(group_id, f'🍾🍾🍾ии.. им становится {d1_sort[0][1]}! Самый главный пидрила черезвычайно'
                                   f' пидарского года!!! {d1_sort[0][1]} прийми наши поздравления, а также '
                                   f'обязательства по амбоссадорству "Голубой устрицы". На ближайший год '
                                   f'на всех наших тусовках ты на разливе ибо больше всех заинтересован поскорее '
                                   f'споить пацанов. Тебе также полагается денежный приз в размере всех денег '
                                   f'накопленных в нашем фонде (в случае их отсутствия возмещаем глубоким '
                                   f'уважением. Хорошего нового года в новом статусе!')
        bot.send_message(group_id, f'За тобой приехали..')
        file = open('gif_zverev.mp4', 'rb')
        bot.send_animation(group_id, file)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    if callback.data == 'btn':
        file2 = open("важно.jpeg", 'rb')
        bot.send_photo(group_id, file2)
    elif callback.data == 'bof':
        start_file = open("ball/start_image.png", 'rb')
        bot.send_photo(callback.message.chat.id, start_file)
        bot.send_message(callback.message.chat.id, '''Решил попытать удачу или просто переложить ответственность?
Что ж.. Чтобы все прошло как надо просто переведи сотку моему создателю на сбер и погладь шар''')
        kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        but1 = types.KeyboardButton(text='Погладить шар')
        but2 = types.KeyboardButton(text='Шар съебись')
        kb1.add(but1, but2)
        bot.send_message(callback.message.chat.id, '...', reply_markup=kb1)
    elif callback.data == 'stat_day':
        load_message = (bot.edit_message_text('Загрузка..⏳', callback.message.chat.id, callback.message.id).message_id)
        kb2 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton(text='Статистика по месяцам', callback_data='stat_month')
        but2 = types.InlineKeyboardButton(text='Статистика по годам', callback_data='stat_year')
        kb2.add(but1, but2)
        bot.edit_message_text(pstat('A'), callback.message.chat.id, load_message)
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id, reply_markup=kb2)
    elif callback.data == 'stat_month':
        load_message = (bot.edit_message_text('Загрузка..⏳', callback.message.chat.id, callback.message.id).message_id)
        kb2 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton(text='Статистика по дням', callback_data='stat_day')
        but2 = types.InlineKeyboardButton(text='Статистика по годам', callback_data='stat_year')
        kb2.add(but1, but2)
        bot.edit_message_text(pstat('C'), callback.message.chat.id, load_message)
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id, reply_markup=kb2)
    elif callback.data == 'stat_year':
        load_message = (bot.edit_message_text('Загрузка..⏳', callback.message.chat.id, callback.message.id).message_id)
        kb2 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton(text='Статистика по дням', callback_data='stat_day', commands=['pidorstat'])
        but2 = types.InlineKeyboardButton(text='Статистика по месяцам', callback_data='stat_month')
        kb2.add(but1, but2)
        bot.edit_message_text(pstat('D'), callback.message.chat.id, load_message)
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id, reply_markup=kb2)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, ('Основные команды поддерживаемые ботом:\n'
                                        '/orel -  вызвать орловского помощника\n'
                                        '/pidorstat - пидорский рейтинг \n'
                                        '/start - инициализация бота\n'
                                        '/help - справка по боту\n'
                                        '/test - тестирование бота'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Бот уже инициализирован.
Я работаю по расписанию. Пидр дня назначается ежедневно 
в 11:00 по московскому времени

/help - справка по боту''')
    
    
@bot.message_handler(commands=['orel'])
def orel(message):
    bot.send_message(message.chat.id, 'Орловский помощник..', reply_markup=kb1)


@bot.message_handler(commands=['pidorstat'])
def test(message):
    b = (bot.send_message(message.chat.id, 'Загрузка..⏳').message_id)
    kb2 = types.InlineKeyboardMarkup(row_width=1)
    but1 = types.InlineKeyboardButton(text='Статистика по месяцам', callback_data='stat_month')
    but2 = types.InlineKeyboardButton(text='Статистика по годам', callback_data='stat_year')
    kb2.add(but1, but2)
    bot.edit_message_text(pstat('A'), message.chat.id, b, reply_markup=kb2)


@bot.message_handler(commands=['test'])
def start(message):
    bot.send_message(message.chat.id, '''Протестируй себя петушок...А моя работа давно проверена и отлажена.

/help - справка по боту''')


@bot.message_handler(commands=['sent_message'])  # команда для переброски клиента из базы потенциальных клиентов в
def sent_message(message):    # базу старых клиентов
    if message.chat.id == admin_id:
        sent = bot.send_message(admin_id, 'Введите текст сообщения')
        bot.register_next_step_handler(sent, sent_message_perehvat)   # перехватывает ответ пользователя на сообщение "sent" и
                                                              # и направляет его аргументом в функцию base_perehvat
    else:
        bot.send_message(message.chat.id, 'У Вас нет прав для использования данной команды')


@bot.message_handler(func=lambda v: v.text)
def chek_message(v):
    if v.text == 'Погладить шар':
        bot.send_photo(v.chat.id, ball_of_fate())
    if v.text == 'Шар съебись':
        kb2 = types.ReplyKeyboardRemove()
        bot.send_message(v.chat.id, '...', reply_markup=kb2)
    if 'Давинчи' in v.text:
        b = str(v.text).replace('Давинчи ', '', 1).replace('Давинчи, ', '', 1).replace('Давинчи,', '', 1).replace(
            ' Давинчи', '', 1)
        Davinci(bot, v, b)
    if 'давинчи' in v.text:
        b = str(v.text).replace('давинчи ', '', 1).replace('давинчи, ', '', 1).replace('давинчи,', '', 1).replace(
            ' давинчи', '', 1)
        Davinci(bot, v, b)
    if 'Артур' in v.text:
        b = str(v.text).replace('Артур ', '', 1).replace('Артур, ', '', 1).replace('Артур,', '', 1).replace(
            ' Артур', '', 1)
        Artur(bot, v, b)
    if 'артур' in v.text:
        b = str(v.text).replace('артур ', '', 1).replace('артур, ', '', 1).replace('артур,', '', 1).replace(
            ' артур', '', 1)
        Artur(bot, v, b)


def sent_message_perehvat(message):
    bot.copy_message(group_id, admin_id, message.id)
    bot.send_message(admin_id, 'Сообщение отправлено!')


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(pidr, "cron", day_of_week='mon-sun', hour=11)
    #scheduler.add_job(pidr, "interval", seconds=10)
    scheduler.start()

    
bot.infinity_polling()
