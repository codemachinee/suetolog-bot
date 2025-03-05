# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher, F, types
import asyncio
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from random import *
from functions_file import value_plus_one, pstat, obnulenie_stat, ball_of_fate, celebrate_day
from FSM import step_message
from SaluteSpeech import *
from yandex_services import *

# token = lemonade
# token = codemashine_test
token = major_suetolog

bot = Bot(token=token)
dp = Dispatcher()

kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Купить билет в Орёл', url='https://жд-билеты.сайт/kupit-zhd-bilety/#/moskva/orel?')],
    [InlineKeyboardButton(text='Бронь стола на Привале', url='http://onmap.uz/tel/74862484006')],
    [InlineKeyboardButton(text='Бронь стола 7 пятниц', url='http://onmap.uz/tel/74862490008')],
    [InlineKeyboardButton(text='Бронь стола Шаривари', url='http://onmap.uz/tel/74862445303')],
    # [InlineKeyboardButton(text='Форма расходов', url='https://forms.gle/MEesbSSkTfpztRrr7')],
    [InlineKeyboardButton(text='Яндекс.Диск', url='https://disk.yandex.ru/client/disk/бот%20суетологов/суетологи')],
    [InlineKeyboardButton(text='Шар судьбы', callback_data='bof')],
    [InlineKeyboardButton(text='Эротический массаж', url='https://egoiste57.ru')]])


async def pidr():
    x = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if x == 1:
        await dr()
        file1 = FSInputFile(r"Я.jpg", 'rb')
        y = ("Игорь", file1)
        await value_plus_one('A2')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''{await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')

    elif x == 2:
        await dr()
        file1 = FSInputFile(r"Филч.jpg", 'rb')
        y = ("Филч", file1)
        await value_plus_one('A1')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''{await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')

    elif x == 3:
        await dr()
        file1 = FSInputFile(r"Серега.jpg", 'rb')
        y = ("Серега", file1)
        await value_plus_one('A3')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''{await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')

    elif x == 4:
        await dr()
        file1 = FSInputFile(r"Леха.jpg", 'rb')
        y = ("Леха(Demix)", file1)
        await value_plus_one('A5')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''{await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')

    elif x == 5:
        await dr()
        file1 = FSInputFile(r"фитиль.jpg", 'rb')
        y = ("Леха(Фитиль)", file1)
        await value_plus_one('A6')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''{await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')

    elif x == 6:
        await dr()
        file1 = FSInputFile(r"маугли.jpg", 'rb')
        y = ("Диман", file1)
        await value_plus_one('A7')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''{await celebrate_day()}
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')

    elif x == 7:
        await dr()
        file1 = FSInputFile(r"саня.jpg", 'rb')
        y = ("Саня", file1)
        await value_plus_one('A4')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''{await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')

    elif x == 8:
        await dr()
        file1 = FSInputFile(r"Кирилл.jpg", 'rb')
        y = ("Кирюха подкастер", file1)
        await value_plus_one('A8')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''{await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')

    elif x == 9:
        await dr()
        file1 = FSInputFile(r"Женек.jpg", 'rb')
        y = ("Женек спасатель", file1)
        await value_plus_one('A9')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''{await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')

    elif x == 10:
        await dr()
        file1 = FSInputFile(r"Евгений.png", 'rb')
        y = ("Женек старый", file1)
        await value_plus_one('A10')
        await bot.send_photo(group_id, y[1])
        await bot.send_message(group_id, f'''{await celebrate_day()} 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')


async def dr():
    await obnulenie_stat(bot)
    if datetime.now().day == 5 and datetime.now().month == 3:
        await Artur_happy_birthday(bot, text=f'Поздравь с днем рождения Кирилла Подкастера с учетом следующих фактов о '
                                           f'нем: 1) Благодаря его стараниям и материалам мы в подробностях '
                                           f'восстанавливаем в памяти все что происходило не смотря на количество '
                                           f'и качество выпитого. '
                                           f'2) Кирилл учится на юриста, но суетой на маркетплейсах решает свои '
                                           f'экономические проблемы. '
                                           f'3) Кирилл всегда готов вписаться в любое приключение, особенно '
                                           f'если это бесплатно. '
                                           f'4) Кирилл прогуливает учебу в ресторанах KFC. '
                                           f'Раньше Кирилл строил из себя циника касаемо амурных вопросов, горячо '
                                           f'отстаивал свои взгляды в спорах с парнями, но судьба увесистой пощечиной '
                                           f'уронила его в отношения и теперь он больше зая, малыш, сладкий и прочее '
                                           f'непотребство. Но мы все все равно желаем счастье нашему новоиспеченному '
                                           f'романтику.'
                                           f'7) Кирилл - это Ахилес, у которого слабое место нос.'
                                           f'8) Кирилл амбасадор пасты и главный критик цен в ресторанах.'
                                           f'9) Кирилл взаимодействует с людьми на основании противопоставлений '
                                           f'и противоречий, поэтому если он вдруг с Вами согласен или ему понравилось'
                                           f'тоже самое что и Вам, берегитесь он что то задумал...'
                                           f'10) Кирилл здорово прогрессировал касательно своего вкуса к пиву - раньше'
                                           f'его любимым пивом являлся томатный сок, теперь он начал пить настоящее.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 20 and datetime.now().month == 4:
        await Artur_pozdravlyaet(bot, text=f'С днем рождения Игоря, с учетом следующих фактов о нем: '
                                           f'1) Игорь поселил тебя Артур в этом чате и дал тебе имя Артур. '
                                           f'2) Игорь беспалевно в какой то момент наполнил этот чат своими '
                                           f'родственниками. 3) Игорь спортсмен и красавчик, парень который мечтал '
                                           f'увидеть и покорить этот мир, но вместо этого сначала пошел в армию а '
                                           f'потом еще и женился чтобы мечты навсегда остались недосигаемыми. '
                                           f'4) Игорь любит спорт и не любит алкоголь но, в последнее время благодаря '
                                           f'его друзьям ситуация кардинально меняется.'
                                           f'5) Игорь думает, что умеет делать все, причем делает это лучше других.'
                                           f'6) Игорь мечтает кому-то устроить "Мальчишник в Вегасе", но получился '
                                           f'только мальчишник в Туле. 7) Игорь латентный анархист, но он чистит'
                                           f'переписки в чатах, поэтому никто не знает.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 27 and datetime.now().month == 4:
        await Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения Алексея Фитиля с учетом следующих фактов о нем: '
                                           f'1) Этот парень настолько легендарный, что его видно издалека. '
                                           f'2) Многие девушки/женщины могут делать ему миньет не вставая на колени, '
                                           f'но они его давно не интересуют. '
                                           f'3) Леха любит бегать, ходить в баню, а после этого всего посещать '
                                           f'макдоналдс. '
                                           f'4) Леха душа компании и человек - настроение, Амбассадор шуток про геев и '
                                           f'российских железных дорог.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 5 and datetime.now().month == 5:
        await Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения Илью с учетом следующих фактов о нем:'
                                           f'1) Илья обладатель фамилии на которую бронируются все столики '
                                           f'заведений где бы мы не находились. 2) Илюха каратист, оптимист и хороший '
                                           f'друг. '
                                           f'2) Если Илюха и перепивает то только Латте и тогда он словно '
                                           f'уходящая умирать в одиночестве кошка,  куда то скрывается чтобы поблевать. '
                                           f'3) Илья водит Форд Фокус и живет в закрытом городе, любит томатное пиво.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 19 and datetime.now().month == 5:
        await Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения Евгения Спасателя с учетом следующих фактов '
                                           f'о нем: 1) Женек выучился на спасателя, обладает пышными волосами и формами, '
                                           f'а также большим опытом работы официантом и охранником. 2) Женек спит, '
                                           f'только когда за рулем и везет пацанов кутить, в остальное время он '
                                           f'либо работает либо пьет. '
                                           f'3) Детство Женек провел на Жилике и сумел выжить там с женской прической '
                                           f'4) Когда Женек устает, он выбирает первую попавшуюся кровать и ломает ее '
                                           f'а после своим храпом распугивает все живое в радиусе 5 км.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 15 and datetime.now().month == 6:
        await Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения Евгения Старого с учетом следующих фактов о нем: '
                                           f'1) Евгений самый старый обитатель чата. '
                                           f'2) Евгений бизнесмен, владелец барбершопов в городе Москва, '
                                           f'который любит активный образ жизни, кататься на сноуборде, плавать на '
                                           f'байдарках, играть в сквош. 3) Женек обожает шутки про геев, готовить '
                                           f'алкогольные коктейли и путешествовать')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 14 and datetime.now().month == 7:
        # elif datetime.now().day == 18 and datetime.now().month == 12:
        await Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения Дмитрия с учетом следующих фактов о нем: '
                                           f'1) Диман полная копия Маугли из сказки Киплинга. '
                                           f'2) Диман скрытый обитатель каменных джунглей, знает толк в кальянах '
                                           f'и кальянщиках.'
                                           f'4) Диман стал реже появляться на наших тусовках о чем мы очень грустим '
                                           f'и хотим чтобы подобное не повторялось.')

        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 16 and datetime.now().month == 7:
        await Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения Сергея, с учетом следующих фактов о нем: '
                                           f'1) Серега часто пропадает, но ярко появляется. 2) Серега спортсмен, '
                                           f'инвестор и тусовщик. 3) Серега помимо того, что на ровне со всеми пьет, '
                                           f'потом садится за руль и развозит всех домой. '
                                           f'4) Серега компанейский парень и душа компании.'
                                           f'5) Серега в последнее время редко появляется на наших тусовках о чем мы '
                                           f'очень грустим и хотим чтобы ситуация исправилась.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 8 and datetime.now().month == 9:
        await Artur_pozdravlyaet(bot, text=f'Поздравь с днем рождения Александра, с учетом следующих фактов о нем: '
                                           f'1) Саня до некоторого времени был самым младшим обитателя нашего '
                                           f'сообщества, но после сориентировался и подтянул еще таких же пиздюков '
                                           f'2) Саня мог бы качественно использовать опыт старших товарищей, '
                                           f'но использовать особо нечего. '
                                           f'3) Саня в душе брокер и криптоинвестор который нагнул мир, но зачем то '
                                           f'пошел учиться на военного и пока нагнул лишь только свои амбиции. '
                                           f'4) Саня стильный, думает что мощный. '
                                           f'5) Саня любит активный отдых, сноуборд, теннис, вейкборд и женщин.')
        await bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 17 and datetime.now().month == 11:
        await Artur_pozdravlyaet(bot,
                                 text=f'Поздравь с днем рождения Алексея с учетом следующих фактов о нем: '
                                      f'1) Леха это стиль и харизма Востока. 2) Леха любит когда все в этой жизни '
                                      f'не дольше 4 минут. '
                                      f'3) Леха любит все что горит и дымит. '
                                      f'4) У Алексея есть хобби и оно заключается в комментировании фильмов под пиво. '
                                      f'5) Леха заботливо следит чтобы все напились как следует и очень '
                                      f'расстраивается если кто то не пьет. 6) Леха бывший успешный тиктокер и '
                                      f'школьный диджей! 6) Леха иногда пытается кулинарить, при этом сам не ест а '
                                      f'только закусывает.')
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
    await bot.send_message(message.chat.id, (f'Основные команды поддерживаемые ботом:\n'
                                             f'/orel - вызвать орловского помощника,\n'
                                             f'/pidorstat - пидорский рейтинг,\n'
                                             f'/start - инициализация бота,\n'
                                             f'/help - справка по боту,\n'
                                             f'/test - тестирование бота.\n\n'
                                             f'Для вызова Давинчи или Артура необходимо указать имя в сообщении.\n\n'
                                             f'Для перевода воиса(длительность до 1 мин.) в текст ответьте на него '
                                             f'словом "давинчи" или перешлите в личку боту.\n\n'
                                             f'Для отправки фото/видео/документа в общую папку на яндекс отправьте '
                                             f'необходимые файлы в личку боту.'))


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
async def sent_message(message, state: FSMContext):  # базу старых клиентов
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
        try:
            if message.reply_to_message.voice.file_id:
                await save_audio(bot, message.reply_to_message)
        except AttributeError:
            b = str(message.text).replace('Давинчи ', '', 1).replace('Давинчи, ', '', 1).replace('Давинчи,', '',
                                                                                             1).replace(
                ' Давинчи', '', 1)
            await Davinci(bot, message, b).answer()
        # else:
        #     await bot.send_message(message.chat.id, 'нет доступа')
    elif 'давинчи' in message.text:
        try:
            if message.reply_to_message.voice.file_id:
                await save_audio(bot, message.reply_to_message)
        except AttributeError:
            b = str(message.text).replace('давинчи ', '', 1).replace('давинчи, ', '',
                                                                     1).replace('давинчи,', '',
                                                                                1).replace(' давинчи', '', 1)
            await Davinci(bot, message, b).answer()
        # else:
        #     await bot.send_message(message.chat.id, 'нет доступа')
    elif 'Артур' in message.text:
        b = str(message.text).replace('Артур ', '', 1).replace('Артур, ', '', 1).replace('Артур,', '', 1).replace(
            ' Артур', '', 1)
        await Artur(bot, message, b)
    elif 'артур' in message.text:
        b = str(message.text).replace('артур ', '', 1).replace('артур, ', '', 1).replace('артур,', '', 1).replace(
            ' артур', '', 1)
        await Artur(bot, message, b)


@dp.message(F.document, F.chat.type == 'private')
async def chek_message(v):
    await YaDisk(bot, v).save_doc()


@dp.message(F.photo, F.chat.type == 'private')
async def chek_message(v):
    await YaDisk(bot, v).save_photo()


@dp.message(F.video, F.chat.type == 'private')
async def chek_message(v):
    await YaDisk(bot, v).save_video()


@dp.message(F.video_note, F.chat.type == 'private')
async def chek_message(v):
    await YaDisk(bot, v).save_video_note()


@dp.message(F.voice, F.chat.type == 'private')
async def chek_message(v):
    await save_audio(bot, v)


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(pidr, "cron", day_of_week='mon-sun', hour=8)
    # scheduler.add_job(pidr, trigger="interval", seconds=15)
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
