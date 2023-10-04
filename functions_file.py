# Импорт необходимых библиотек и модулей
import gspread
import yadisk
import g4f
from datetime import datetime
from random import *
from aiogram.types import FSInputFile
from paswords import *

# Инициализация YaDisk
y = yadisk.YaDisk(token=yadisk_token)

# Списки для сохранения сообщений от Давинчи и Артура, а также провайдеров
saved_messages_davinci = []
saved_messages_artur = []
provider_list = [g4f.Provider.CodeLinkAva, g4f.Provider.Ails,
                 g4f.Provider.ChatgptAi, g4f.Provider.DeepAi, g4f.Provider.H2o]


# Функция для увеличения значения ячейки на 1
async def value_plus_one(j):
    gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
    sh = gc.open("bot_statistic")
    worksheet = sh.get_worksheet(0)
    worksheet.update(j, str(int(worksheet.acell(j).value) + 1))


# Функция для формирования статистики
async def pstat(cell):
    # Подключение к Google Sheets API
    gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')

    # Открытие Google Sheets документа
    sh = gc.open("bot_statistic")
    worksheet = sh.get_worksheet(0)

    # Сбор данных по статистике пидоров
    d1 = [
        (int(worksheet.acell(f'{cell}1').value), "Филч"),
        (int(worksheet.acell(f'{cell}2').value), "Игорь"),
        (int(worksheet.acell(f'{cell}3').value), "Серега"),
        (int(worksheet.acell(f'{cell}4').value), "Саня"),
        (int(worksheet.acell(f'{cell}5').value), "Леха(Саня)"),
        (int(worksheet.acell(f'{cell}6').value), "Леха(Фитиль)"),
        (int(worksheet.acell(f'{cell}7').value), "Диман"),
        (int(worksheet.acell(f'{cell}8').value), "Кирюха подкастер"),
        (int(worksheet.acell(f'{cell}9').value), "Женек спасатель"),
        (int(worksheet.acell(f'{cell}10').value), "Женек старый")
    ]

    # Сортировка данных по количеству пидорских действий
    d1_sort = sorted(d1, reverse=True)

    # Формирование сообщения с рейтингом пидоров
    return (f'''РЕЙТИНГ ПИДАРАСОВ:

    1. {d1_sort[0][1]} -----> {d1_sort[0][0]} раз(а)
    2. {d1_sort[1][1]} -----> {d1_sort[1][0]} раз(а)
    3. {d1_sort[2][1]} -----> {d1_sort[2][0]} раз(а)
    4. {d1_sort[3][1]} -----> {d1_sort[3][0]} раз(а)
    5. {d1_sort[4][1]} -----> {d1_sort[4][0]} раз(а)
    6. {d1_sort[5][1]} -----> {d1_sort[5][0]} раз(а)
    7. {d1_sort[6][1]} -----> {d1_sort[6][0]} раз(а)
    8. {d1_sort[7][1]} -----> {d1_sort[7][0]} раз(а)
    9. {d1_sort[8][1]} -----> {d1_sort[8][0]} раз(а)
    10. {d1_sort[9][1]} -----> {d1_sort[9][0]} раз(а)

    Да здравствует наш чемпион {d1_sort[0][1]}! Его результативности 
    может позавидовать Элтон Джон и другие Великие. Пожелаем
    ему здоровья, успехов в личной жизни и новых побед.

    /help - справка по боту''')


# функция обнуляющая все значения статистики в первый день нового месяца
async def obnulenie_stat(bot):
    # Создание списка для хранения победителей
    champions = []

    # Проверка на начало нового месяца
    if datetime.now().day == 1 and datetime.now().month != 1:
        # Подключение к Google Sheets API
        gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
        sh = gc.open("bot_statistic")
        worksheet = sh.get_worksheet(0)

        # Получение данных из таблицы
        d1 = [(int(worksheet.acell('A1').value), "Филч"), (int(worksheet.acell('A2').value), "Игорь"),
              (int(worksheet.acell('A3').value), "Серега"), (int(worksheet.acell('A4').value), "Саня"),
              (int(worksheet.acell('A5').value), "Леха(Саня)"), (int(worksheet.acell('A6').value), "Леха(Фитиль)"),
              (int(worksheet.acell('A7').value), "Диман"), (int(worksheet.acell('A8').value), "Кирюха подкастер"),
              (int(worksheet.acell('A9').value), "Женек спасатель"),
              (int(worksheet.acell('A10').value), "Женек старый")]

        # Сортировка данных по количеству пидорских действий
        d1_sort = sorted(d1, reverse=True)

        # Поиск ячеек с победителем
        cells = worksheet.findall(d1_sort[0][0], in_column=1)
        for cell in cells:
            # Обновление данных в таблице
            worksheet.update(f'C{cell.row}', f'{int(worksheet.acell(f"C{cell.row}").value) + 1}')
            champions.append(str(worksheet.acell(f"B{cell.row}").value))

        # Формирование сообщения с итогами месяца
        if len(champions) == 1:
            await bot.send_message(group_id, f'''ИТОГИ МЕСЯЦА:

             1. {d1_sort[0][1]} -----> {d1_sort[0][0]} раз(а)
             2. {d1_sort[1][1]} -----> {d1_sort[1][0]} раз(а)
             ... (аналогично для других мест)
             10. {d1_sort[9][1]} -----> {d1_sort[9][0]} раз(а)

            Да здравствует наш чемпион месяца {d1_sort[0][1]}🎉🎉🎉! 
            В тяжелейшей борьбе он таки вырвал свою заслуженную победу. 
            Пожелаем ему здоровья, успехов в личной жизни и новых побед.''')
        else:
            await bot.send_message(group_id, f'''ИТОГИ МЕСЯЦА:

                         1. {d1_sort[0][1]} -----> {d1_sort[0][0]} раз(а)
                         2. {d1_sort[1][1]} -----> {d1_sort[1][0]} раз(а)
                         ... (аналогично для других мест)
                         10. {d1_sort[9][1]} -----> {d1_sort[9][0]} раз(а)

            Да здравствует наши чемпионы месяца {", ".join(champions)}! 
            В тяжелейшей борьбе они таки вырвали свою заслуженную победу. 
            Пожелаем им здоровья, успехов в личной жизни и новых побед.''')

        # Обнуление данных в таблице
        worksheet.update('A1:A10', [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])

    # Проверка на конец года
    elif datetime.now().day == 31 and datetime.now().month == 12:
        # Отправка уведомления о подведении итогов года
        await bot.send_message(group_id, f'🚨🚨🚨Внимание!🚨🚨🚨 Пидр Клаус подводит итоги...\n'
                                         f'Кто же станет пидаром года?')
        # Отправка видео
        file = FSInputFile(r'gif_mr.Bin.mp4', 'rb')
        await bot.send_video(group_id, file)

        # Подключение к Google Sheets API
        gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
        sh = gc.open("bot_statistic")
        worksheet = sh.get_worksheet(0)

        # Получение данных из таблицы
        d1 = [(int(worksheet.acell('C1').value), "Филч"), (int(worksheet.acell('C2').value), "Игорь"),
              (int(worksheet.acell('C3').value), "Серега"), (int(worksheet.acell('C4').value), "Саня"),
              (int(worksheet.acell('C5').value), "Леха(Саня)"), (int(worksheet.acell('C6').value), "Леха(Фитиль)"),
              (int(worksheet.acell('C7').value), "Диман"), (int(worksheet.acell('C8').value), "Кирюха подкастер"),
              (int(worksheet.acell('C9').value), "Женек спасатель"),
              (int(worksheet.acell('C10').value), "Женек старый")]

        # Сортировка данных по количеству пидорских действий
        d1_sort = sorted(d1, reverse=True)

        # Поиск ячеек с победителем
        cells = worksheet.findall(str(d1_sort[0][0]), in_column=3)
        for cell in cells:
            # Обновление данных в таблице
            worksheet.update(f'D{cell.row}', f'{int(worksheet.acell(f"D{cell.row}").value) + 1}')
            champions.append(str(worksheet.acell(f"B{cell.row}").value))

        # Формирование сообщения с итогами года
        if len(champions) == 1:
            await bot.send_message(group_id, f'🍾🍾🍾ии.. им становится {d1_sort[0][1]}! '
                                             f'Самый главный пидрила черезвычайно пидарского года!!! '
                                             f'{d1_sort[0][1]} прийми наши поздравления, а также '
                                             f'обязательства по амбассадорству "Голубой устрицы". '
                                             f'На ближайший год на всех наших тусовках ты на разливе ибо больше всех '
                                             f'заинтересован поскорее споить пацанов. Тебе также полагается денежный приз '
                                             f'в размере всех денег накопленных в нашем фонде (в случае их отсутствия '
                                             f'возмещаем глубоким уважением. Хорошего нового года в новом статусе!')
            await bot.send_message(group_id, f'''ИТОГИ ГОДА:

                             1. {d1_sort[0][1]} -----> {d1_sort[0][0]} раз(а) 🎉🎉🎉
                             ... (аналогично для других мест)
                             10. {d1_sort[9][1]} -----> {d1_sort[9][0]} раз(а)

            Да здравствует наш ПИДАРАС года {d1_sort[0][1]}! 
            В тяжелейшей борьбе он таки вырвал свою заслуженную победу. 
            Пожелаем ему здоровья, успехов в личной жизни и новых побед.''')
            await bot.send_message(group_id, f'За тобой приехали..')
            file = FSInputFile(r'gif_zverev.mp4', 'rb')
            await bot.send_video(group_id, file)
        else:
            await bot.send_message(group_id, f'🍾🍾🍾ии.. ими становится {", ".join(champions)}! '
                                             f'Выдающиеся пидрилы черезвычайно пидарского года!!! '
                                             f'{", ".join(champions)} приймите наши поздравления, а также '
                                             f'обязательства по амбассадорству "Голубой устрицы". '
                                             f'На ближайший год на всех наших тусовках вы на разливе ибо больше всех '
                                             f'заинтересованы поскорее споить пацанов. Вам также полагается денежный приз '
                                             f'в размере всех денег накопленных в нашем фонде (в случае их отсутствия '
                                             f'возмещаем глубоким уважением. Хорошего Нового года в новом статусе!')
            await bot.send_message(group_id, f'''ИТОГИ ГОДА:

                            1. {d1_sort[0][1]} -----> {d1_sort[0][0]} раз(а)
                            ... (аналогично для других мест)
                            10. {d1_sort[9][1]} -----> {d1_sort[9][0]} раз(а)

Да здравствует наши ПИДАРАСы года {", ".join(champions)}🎉🎉🎉! 
В тяжелейшей борьбе они таки вырвали свою заслуженную победу. 
Пожелаем им здоровья, успехов в личной жизни и новых побед.''')
            await bot.send_message(group_id, f'За вами приехали..')
            file = FSInputFile(r'gif_zverev.mp4', 'rb')
            await bot.send_video(group_id, file)

        # Обнуление данных в таблице
        worksheet.update('A1:A10', [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])
        worksheet.update('C1:C10', [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])
        await bot.send_message(group_id, f'За тобой приехали..')
        file = FSInputFile(r'gif_zverev.mp4', 'rb')
        await bot.send_video(group_id, file)
    else:
        pass


# Функция для празднования различных "пидарасов" в зависимости от даты
async def celebrate_day():
    if datetime.now().day == 31 and datetime.now().month == 12:
        return '🎉Новогодним пидарасом🎉'
    elif datetime.now().day == 7 and datetime.now().month == 1:
        return '🎉Рождественским пидарасом🎉'
    elif datetime.now().day == 14 and datetime.now().month == 1:
        return '🎉Староновогодним пидарасом🎉'
    elif datetime.now().day == 14 and datetime.now().month == 2:
        return '🎉Личным пидарасом Валентина🎉'
    elif datetime.now().day == 23 and datetime.now().month == 2:
        return '🎉Защищенным пидарасом🎉'
    elif datetime.now().day == 8 and datetime.now().month == 3:
        return '🎉Международным женским пидарасом🎉'
    elif datetime.now().day == 1 and datetime.now().month == 5:
        return '🎉Мирным трудолюбивым и майским пидарасом🎉'
    elif datetime.now().day == 1 and datetime.now().month == 9:
        return '🎉Школьным пидарасом🎉'
    elif datetime.now().day == 4 and datetime.now().month == 11:
        return '🎉Народным пидарасом🎉'
    else:
        return 'Пидарасом дня'


# Функция "шара судьбы", которая возвращает случайное изображение шара с ответом
async def ball_of_fate():
    ball_choice = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    if ball_choice == 1:
        ball_answer = FSInputFile(r"ball/var_one.png", 'rb')
        return ball_answer
    elif ball_choice == 2:
        ball_answer = FSInputFile(r"ball/var_two.png", 'rb')
        return ball_answer
    elif ball_choice == 3:
        ball_answer = FSInputFile(r"ball/var_tree.png", 'rb')
        return ball_answer
    # Для каждого возможного варианта ответа выбирается соответствующее изображение шара
    # (в данном случае, используются файлы с изображениями var_one.png, var_two.png и т. д.)
    elif ball_choice == 4:
        ball_answer = FSInputFile(r"ball/var_four.png", 'rb')
        return ball_answer
    elif ball_choice == 5:
        ball_answer = FSInputFile(r"ball/var_five.png", 'rb')
        return ball_answer
    elif ball_choice == 6:
        ball_answer = FSInputFile(r"ball/var_six.png", 'rb')
        return ball_answer
    elif ball_choice == 7:
        ball_answer = FSInputFile(r"ball/var_seven.png", 'rb')
        return ball_answer
    elif ball_choice == 8:
        ball_answer = FSInputFile(r"ball/var_eight.png", 'rb')
        return ball_answer
    elif ball_choice == 9:
        ball_answer = FSInputFile(r"ball/var_nine.png", 'rb')
        return ball_answer
    elif ball_choice == 10:
        ball_answer = FSInputFile(r"ball/var_ten.png", 'rb')
        return ball_answer
    elif ball_choice == 11:
        ball_answer = FSInputFile(r"ball/var_eleven.png", 'rb')
        return ball_answer


class Davinci:
    # Глобальные переменные для сохранения сообщений и списка провайдеров
    global saved_messages_davinci
    global provider_list

    # Конструктор класса, принимающий бота, сообщение и текст
    def __init__(self, bot, message, text):
        self.bot = bot
        self.message = message
        self.text = text

    # Асинхронная функция ответа
    async def answer(self):
        try:
            # Вставляем текущее сообщение пользователя в список сохраненных сообщений
            saved_messages_davinci.insert(0, f'Вы: {self.text}\n')
            # Создаем "промпт" для модели, переворачивая сохраненные сообщения
            prompt_davinci = (''.join(reversed(saved_messages_davinci)))
            # Отправляем сообщение о том, что ответ формируется
            await self.bot.send_message(self.message.chat.id, f'секунду..')
            # Запрашиваем ответ у модели, используя GPT-3.5
            response = await g4f.ChatCompletion.create_async(
                model=g4f.models.default,
                messages=[{"role": "user", "content": f'{prompt_davinci}'}],
                provider=choice(provider_list))
            # Отправляем полученный ответ пользователю
            await self.bot.send_message(self.message.chat.id, f'{response}')
            # Вставляем ответ в список сохраненных сообщений
            saved_messages_davinci.insert(0, f'{str(response)}\n')
            # Если в списке сохраненных сообщений более 8 элементов, удаляем лишние
            if len(saved_messages_davinci) >= 8:
                del saved_messages_davinci[3:]
        except Exception:
            # Если возникла ошибка, отправляем сообщение о перерыве
            await self.bot.send_message(self.message.chat.id, "Простите, но мне нужен перекур..")
            # Удаляем сохраненные сообщения, кроме первого
            del saved_messages_davinci[1:]


# class Artur:
#     global saved_messages_artur
#     global provider_list
#
#     def __init__(self, bot, message, text):
#         try:
#             self.bot = bot
#             self.message = message
#             self.text = text
#             answer_model = open('Artur_mini.txt', 'r', encoding='utf-8')
#             saved_messages_artur.insert(0, f'Вы: {self.text}\n')
#             prompt_text = (str(answer_model.read()) + ''.join(reversed(saved_messages_artur)))
#             self.bot.send_message(message.chat.id, f'секунду..')
#             response = g4f.ChatCompletion.create(
#                 model=g4f.models.default,
#                 messages=[{"role": "user", "content": f'{prompt_text}'}],
#                 provider=(choice(provider_list)),
#                 stream=False)
#             self.bot.send_message(message.chat.id, f'{response}')
#             saved_messages_artur.insert(0, f'{str(response)}\n')
#             if len(saved_messages_artur) >= 6:
#                 del saved_messages_artur[3:]
#         except Exception:
#             self.bot.send_message(message.chat.id, "Занимайся..")
#             del saved_messages_artur[1:]


async def Artur_pozdravlyaet(bot, text):
    try:
        # Создаем "промпт" для модели, используя переданный текст
        prompt_text = text
        # Запрашиваем ответ у модели, используя GPT-3.5
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": f'{prompt_text}'}],
            provider=choice(provider_list))
        # Отправляем полученный ответ пользователю в группу
        await bot.send_message(group_id, f'{response}')
    except Exception:
        # Если возникла ошибка, повторно вызываем функцию для попытки повторного запроса
        await Artur_pozdravlyaet(bot, text)
        # Удаляем сохраненные сообщения, кроме первого
        del saved_messages_artur[1:]


# Класс для работы с Яндекс.Диск
class YaDisk:

    # Инициализация объекта
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    # Асинхронная функция для сохранения фото на Яндекс.Диск
    async def save_photo(self):
        try:
            # Отправляем сообщение о начале загрузки
            await self.bot.send_message(self.message.chat.id, 'Загружаю...')
            file_id = self.message.photo[-1].file_id
            file = await self.bot.get_file(file_id)
            file_path = file.file_path
            src = f'/суетологи/{datetime.now().day}.{datetime.now().month}.{datetime.now().year}'

            # Проверяем, существует ли указанный путь на Яндекс.Диске
            if y.exists(src) is False:
                y.mkdir(src)

            # Загружаем фото на Яндекс.Диск
            y.upload(await self.bot.download_file(file_path),
                     f'{src}/{datetime.now().hour}.{datetime.now().minute}.{datetime.now().second}.jpg')
            # Отправляем сообщение об успешной загрузке
            await self.bot.send_message(self.message.chat.id, 'Фото успешно загружено')

        except Exception:
            # В случае ошибки отправляем сообщение об ошибке
            await self.bot.send_message(self.message.chat.id, 'Отправка не удалась')

    # Асинхронная функция для сохранения документа на Яндекс.Диск
    async def save_doc(self):
        try:
            # Отправляем сообщение о начале загрузки
            await self.bot.send_message(self.message.chat.id, 'Загружаю...')
            file_id = self.message.document.file_id
            file = await self.bot.get_file(file_id)
            file_path = file.file_path
            src = f'/суетологи/{datetime.now().day}.{datetime.now().month}.{datetime.now().year}'

            # Проверяем, существует ли указанный путь на Яндекс.Диске
            if y.exists(src) is False:
                y.mkdir(src)

            # Загружаем документ на Яндекс.Диск
            y.upload(await self.bot.download_file(file_path),
                     f'{src}/{self.message.document.file_name}')
            # Отправляем сообщение об успешной загрузке
            await self.bot.send_message(self.message.chat.id, 'Документ успешно загружен')

        except Exception:
            # В случае ошибки отправляем сообщение об ошибке
            await self.bot.send_message(self.message.chat.id, 'Отправка не удалась')

    # Асинхронная функция для сохранения видео на Яндекс.Диск
    async def save_video(self):
        try:
            # Отправляем сообщение о начале загрузки
            await self.bot.send_message(self.message.chat.id, 'Загружаю...')
            file_id = self.message.video.file_id
            file = await self.bot.get_file(file_id)
            file_path = file.file_path
            src = f'/суетологи/{datetime.now().day}.{datetime.now().month}.{datetime.now().year}'

            # Проверяем, существует ли указанный путь на Яндекс.Диске
            if y.exists(src) is False:
                y.mkdir(src)

            # Загружаем видео на Яндекс.Диск
            y.upload(await self.bot.download_file(file_path),
                     f'{src}/{self.message.video.file_name}')
            # Отправляем сообщение об успешной загрузке
            await self.bot.send_message(self.message.chat.id, 'Видео успешно загружено')

        except Exception:
            # В случае ошибки отправляем сообщение об ошибке
            await self.bot.send_message(self.message.chat.id, 'Отправка не удалась')
