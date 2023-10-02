# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher, F, types
import asyncio
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from random import *
from functions_file import value_plus_one, pstat, obnulenie_stat, ball_of_fate, Davinci, celebrate_day, \
    Artur_pozdravlyaet, YaDisk
from FSM import step_message
from paswords import *

#token = lemonade
# token = codemashine_test
token = major_suetolog

bot = Bot(token=token)
dp = Dispatcher()

kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Купить билет в Орёл', url='https://жд-билеты.сайт/kupit-zhd-bilety/#/moskva/orel?')],
    [InlineKeyboardButton(text='Бронь стола на Привале', url='http://onmap.uz/tel/74862484006')],
    [InlineKeyboardButton(text='Бронь стола 7 пятниц', url='http://onmap.uz/tel/74862490008')],
    [InlineKeyboardButton(text='Бронь стола Шаривари', url='http://onmap.uz/tel/74862445303')],
    [InlineKeyboardButton(text='Форма расходов', url='https://forms.gle/MEesbSSkTfpztRrr7')],
    [InlineKeyboardButton(text='Яндекс.Диск', url='https://disk.yandex.ru/client/disk/бот%20суетологов/суетологи')],
    [InlineKeyboardButton(text='Шар судьбы', callback_data='bof')],
    [InlineKeyboardButton(text='Игровой чат', url='http://178.57.222.84/http://178.57.222.84/')]])


async def pidr():
    x = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if x == 1:
        file1 = FSInputFile(r"Я.jpg", 'rb')
        y = ("Игорь", file1)
        await value_plus_one('A2')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''Всем привет!!! {await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        await dr()

    elif x == 2:
        file1 = FSInputFile(r"Филч.jpg", 'rb')
        y = ("Филч", file1)
        await value_plus_one('A1')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''Всем привет!!! {await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        await dr()

    elif x == 3:
        file1 = FSInputFile(r"Серега.jpg", 'rb')
        y = ("Серега", file1)
        await value_plus_one('A3')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''Всем привет!! {await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        await dr()

    elif x == 4:
        file1 = FSInputFile(r"Леха.jpg", 'rb')
        y = ("Леха(Саня)", file1)
        await value_plus_one('A5')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''Всем привет!! {await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        await dr()

    elif x == 5:
        file1 = FSInputFile(r"фитиль.jpg", 'rb')
        y = ("Леха(Фитиль)", file1)
        await value_plus_one('A6')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''Всем привет!! {await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        await dr()

    elif x == 6:
        file1 = FSInputFile(r"маугли.jpg", 'rb')
        y = ("Диман", file1)
        await value_plus_one('A7')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''Всем привет!! {await celebrate_day()}
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        await dr()

    elif x == 7:
        file1 = FSInputFile(r"саня.jpg", 'rb')
        y = ("Саня", file1)
        await value_plus_one('A4')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''Всем привет!! {await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        await dr()

    elif x == 8:
        file1 = FSInputFile(r"Кирилл.jpg", 'rb')
        y = ("Кирюха подкастер", file1)
        await value_plus_one('A8')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''Всем привет!! {await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        await dr()

    elif x == 9:
        file1 = FSInputFile(r"Женек.jpg", 'rb')
        y = ("Женек спасатель", file1)
        await value_plus_one('A9')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''Всем привет!! {await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        await dr()

    elif x == 10:
        file1 = FSInputFile(r"Евгений.png", 'rb')
        y = ("Женек старый", file1)
        await value_plus_one('A10')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''Всем привет!! {await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        await dr()


async def dr():
    await obnulenie_stat(bot)
    if datetime.now().day == 6 and datetime.now().month == 3:
        await Artur_pozdravlyaet(bot, text=f'На русском языке в сатирической форме поздравь с днем рождения Кирилла '
                                                                f'Подкастера - Великого венчестера нашего коллектива. '
                                    f'Благодаря его стараниям и материалам мы в подробностях '
                                    f'восстанавливаем в памяти все что происходило не смотря на количество и качество '
                                    f'выпитого. Кирилл учится на юриста и до сих пор любит свою бывшую девушку'
                                    f'Лизу, но всячески это отрицает. Всегда вписывается в любое приключение, особенно '
                                    f'если это бесплатно. Прогуливает учебу в ресторанах KFC.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 20 and datetime.now().month == 4:
        await Artur_pozdravlyaet(bot, text=f'На русском языке в сатирической форме поздравь с днем рождения Игоря, '
                                                                f'который поселил тебя в этом чате, '
                                                                f'а также беспалевно наполнил его своими родственниками.'
                                                                f'Игорь спортсмен и красавчик, парень который мечтал '
                                                                f'увидеть и покорить этот мир, но вместо этого сначала '
                                                                f'пошел в армию а потом еще и женился чтобы мечты '
                                                                f'навсегда остались недосигаемыми.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 27 and datetime.now().month == 4:
        await Artur_pozdravlyaet(bot, text=f'На русском языке в сатирической форме поздравь с днем рождения Алексея '
                                                                f'Фитиля. Этот парень настолько легендарный, что его '
                                                                f'видно издалека. '
                                          f'Многие девушки/женщины могут делать ему миньет не вставая на колени, но они'
                                          f' его давно не интересуют.. Леха любит бегать, ходить в баню, а после этого'
                                                                f'всего посещать макдоналдс. Леха душа компании и '
                                                                f'человек - настроение, Амбассадор шуток про геев и '
                                                                f'российских железных дорог.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 5 and datetime.now().month == 5:
        await Artur_pozdravlyaet(bot, text=f'На русском языке в сатирической форме поздравь с днем рождения Илью '
                                                                f'обладателя фамилии на которую бронируются все столики '
                                                                f'заведений города Орел. Илюха каратист, оптимист и '
                                                                f'хороший друг. Если Илюха перепивает, то он словно '
                                                                f'уходящая умирать в одиночестве кошка,  куда то скрывается '
                                                                f'чтобы поблевать. Илья водит Форд Фокус и живет в '
                                                                f'закрытом городе, любит томатное пиво.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 19 and datetime.now().month == 5:
        await Artur_pozdravlyaet(bot, text=f'На русском языке в сатирической форме поздравь с днем рождения Евгения '
                                                                f'Спасателя. Женек учится на спасателя, обладает пышными'
                                                                f'волосами, большим опытом работы официантом. Женек '
                                                                f'спит, только когда за рулем и везет пацанов в город '
                                                                f'Орел, в остальное время он либо работает либо пьет. '
                                                                f'Детство провел на Жилике и выжил там с женской '
                                                                f'прической')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 15 and datetime.now().month == 6:
        await Artur_pozdravlyaet(bot, text=f'На русском языке в сатирической форме поздравь с днем рождения Евгения '
                                                                f'Евгений самый старый обитатель чата, '
                                                                f'бизнесмен, владелец барбершопов в '
                                                                f'городе Москва, который любит активный образ жизни, '
                                                                f'кататься на сноуборде, плавать на байдарках, играть '
                                                                f'в сквош, а еще обожает шутки про геев, готовить '
                                                                f'алкогольные коктейли и путешествовать')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 14 and datetime.now().month == 7:
        await Artur_pozdravlyaet(bot, text=f'На русском языке в сатирической форме поздравь с днем рождения Дмитрия,'
                                                                f'Диман копия Маугли из сказки Киплинга. '
                                                                f'Диман скрытый обитатель каменных джунглей, знает толк '
                                                                f'в кальянах и кальянщиках. Диман один из немногих в '
                                                                f'нашем чате кто уже стал отцом, однако умнее и '
                                                                f'серьезнее он от этого не стал!')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 16 and datetime.now().month == 7:
        await Artur_pozdravlyaet(bot, text=f'На русском языке в сатирической форме поздравь с днем рождения Сергея, '
                                                                f'который часто пропадает, но ярко появляется. Серега'
                                                                f'спортсмен, инвестор и тусовщик. Серега помимо того, '
                                                                f'что на ровне со всеми пьет, потом садится за '
                                                                f'руль и развозит их домой. Серега компанейский парень '
                                                                f'и душа компании.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 8 and datetime.now().month == 9:
        await Artur_pozdravlyaet(bot, text=f'На русском языке в сатирической форме поздравь с днем рождения Александра, '
                                                                f'самого младшего обитателя нашего сообщества, который '
                                                                f'мог бы качественно использовать опыт старших товарищей, '
                                                                f'но использовать особо нечего. Саня в душе брокер '
                                                                f'который нагнул мир, но зачем то пошел учиться на '
                                                                f'военного и пока нагнул лишь только свои амбиции. Саня '
                                                                f'стильный, думает что мощный. Саня любит активный '
                                                                f'отдых, сноуборд, теннис, вейкборд и женщин. Саня '
                                                                f'пытается использовать '
                                                                f'свободу по полному но она ограничена отпуском')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 17 and datetime.now().month == 11:
    # elif datetime.now().day == 26 and datetime.now().month == 9:
        await Artur_pozdravlyaet(bot, text=f'На русском языке в сатирической форме поздравь с днем рождения Алексея'
                                                                f'Леха это стиль и харизма Востока. Леха любит когда все '
                                                                f'в этой жизни не дольше 4 минут. Леха любит все что '
                                                                f'горит и дымит. Леха заботливо следит чтобы все '
                                                                f'напились как следует и очень расстраивается если кто'
                                                                f'то не пьет. Леха бывший успешный тиктокер и школьный '
                                                                f'диджей!')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')


@dp.callback_query(F.data)
async def check_callback(callback: CallbackQuery):
    if callback.data == 'bof':
        start_file = FSInputFile(r"ball/start_image.png", 'rb')
        await bot.send_photo(callback.message.chat.id, start_file)
        await bot.send_message(callback.message.chat.id, '''Решил попытать удачу или просто переложить ответственность?
Что ж.. Чтобы все прошло как надо просто переведи сотку моему создателю на сбер и погладь шар''')
        kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, keyboard=[
            [types.KeyboardButton(text='Погладить шар')],
            [types.KeyboardButton(text='Шар съебись')]])
        await bot.send_message(callback.message.chat.id, '...', reply_markup=kb1)
    elif callback.data == 'stat_day':
        load_message = await bot.edit_message_text('Загрузка..⏳', callback.message.chat.id, callback.message.message_id)
        kb2 = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [InlineKeyboardButton(text='Статистика по месяцам', callback_data='stat_month')],
            [InlineKeyboardButton(text='Статистика по годам', callback_data='stat_year')]])
        await bot.edit_message_text(await pstat('A'), callback.message.chat.id, load_message.message_id)
        await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=kb2)
    elif callback.data == 'stat_month':
        load_message = await bot.edit_message_text('Загрузка..⏳', callback.message.chat.id, callback.message.message_id)
        kb2 = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [InlineKeyboardButton(text='Статистика по дням', callback_data='stat_day')],
            [InlineKeyboardButton(text='Статистика по годам', callback_data='stat_year')]])
        await bot.edit_message_text(await pstat('C'), callback.message.chat.id, load_message.message_id)
        await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=kb2)
    elif callback.data == 'stat_year':
        load_message = await bot.edit_message_text('Загрузка..⏳', callback.message.chat.id, callback.message.message_id)
        kb2 = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
            [InlineKeyboardButton(text='Статистика по дням', callback_data='stat_day')],
            [InlineKeyboardButton(text='Статистика по месяцам', callback_data='stat_month')]])
        await bot.edit_message_text(await pstat('D'), callback.message.chat.id, load_message.message_id)
        await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=kb2)


@dp.message(Command(commands='help'))
async def help(message):
    await bot.send_message(message.chat.id, ('Основные команды поддерживаемые ботом:\n'
                                             '/orel -  вызвать орловского помощника\n'
                                             '/pidorstat - пидорский рейтинг \n'
                                             '/start - инициализация бота\n'
                                             '/help - справка по боту\n'
                                             '/test - тестирование бота'))


@dp.message(Command(commands='start'))
async def start(message):
    await bot.send_message(message.chat.id, '''Бот уже инициализирован.
Я работаю по расписанию. Пидр дня назначается ежедневно 
в 11:00 по московскому времени

/help - справка по боту''')
    
    
@dp.message(Command(commands='orel'))
async def orel(message):
    await bot.send_message(message.chat.id, 'Орловский помощник..', reply_markup=kb1)


@dp.message(Command(commands='pidorstat'))
async def stat(message):
    b = await bot.send_message(message.chat.id, 'Загрузка..⏳')
    kb2 = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [InlineKeyboardButton(text='Статистика по месяцам', callback_data='stat_month')],
        [InlineKeyboardButton(text='Статистика по годам', callback_data='stat_year')]])
    await bot.edit_message_text(await pstat('A'), message.chat.id, b.message_id, reply_markup=kb2)


@dp.message(Command(commands='test'))
async def test(message):
    await bot.send_message(message.chat.id, '''Протестируй себя петушок...А моя работа давно проверена и отлажена.

/help - справка по боту''')


@dp.message(Command(commands='sent_message'))  # команда для переброски клиента из базы потенциальных клиентов в
async def sent_message(message, state: FSMContext):    # базу старых клиентов
    if message.chat.id == admin_id:
        await bot.send_message(admin_id, 'Введите текст сообщения')
        await state.set_state(step_message.message)

    else:
        await bot.send_message(message.chat.id, 'У Вас нет прав для использования данной команды')


@dp.message(step_message.message)
async def perehvat(message, state: FSMContext):
    await bot.copy_message(group_id, admin_id, message.message_id)
    await Message.answer(message, text='сообщение отправлено', show_allert=True)
    await state.clear()


@dp.message(F.text)
async def chek_message(message):
    if message.text == 'Погладить шар':
        await bot.send_photo(message.chat.id, await ball_of_fate())
    elif message.text == 'Шар съебись':
        kb2 = types.ReplyKeyboardRemove()
        await bot.send_message(message.chat.id, '...', reply_markup=kb2)
    elif 'Давинчи' in message.text:
        if message.chat.id == admin_id:
            b = str(message.text).replace('Давинчи ', '', 1).replace('Давинчи, ', '', 1).replace('Давинчи,', '', 1).replace(
                ' Давинчи', '', 1)
            await Davinci(bot, message, b).answer()
        else:
            await bot.send_message(message.chat.id, 'нет доступа')
    elif 'давинчи' in message.text:
        if message.chat.id == admin_id:
            b = str(message.text).replace('давинчи ', '', 1).replace('давинчи, ', '', 1).replace('давинчи,', '', 1).replace(
                ' давинчи', '', 1)
            await Davinci(bot, message, b).answer()
        else:
            await bot.send_message(message.chat.id, 'нет доступа')
    # if 'Артур' in v.text:
    #     b = str(v.text).replace('Артур ', '', 1).replace('Артур, ', '', 1).replace('Артур,', '', 1).replace(
    #         ' Артур', '', 1)
    #     Artur(bot, v, b)
    # if 'артур' in v.text:
    #     b = str(v.text).replace('артур ', '', 1).replace('артур, ', '', 1).replace('артур,', '', 1).replace(
    #         ' артур', '', 1)
    #     Artur(bot, v, b)


@dp.message(F.document, F.chat.type == 'private')
async def chek_message(v):
    await YaDisk(bot, v).save_doc()


@dp.message(F.photo, F.chat.type == 'private')
async def chek_message(v):
    await YaDisk(bot, v).save_photo()


@dp.message(F.video, F.chat.type == 'private')
async def chek_message(v):
    await YaDisk(bot, v).save_video()


# def sent_message_perehvat(message):
#     bot.copy_message(group_id, admin_id, message.id)
#     bot.send_message(admin_id, 'Сообщение отправлено!')


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(pidr, "cron", day_of_week='mon-sun', hour=11)
    # scheduler.add_job(pidr, trigger="interval", seconds=15)
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')


