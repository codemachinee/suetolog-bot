# библиотека работы с гугл таблицами
import gspread
import g4f
# библиотека проверки даты
from datetime import datetime
# библиотека рандома
from random import *
from paswords import *

saved_messages_davinci = []
saved_messages_artur = []
provider_list = [g4f.Provider.Aichat, g4f.Provider.Aivvm, g4f.Provider.CodeLinkAva, g4f.Provider.Vitalentum,
                 g4f.Provider.Ylokh]


# функция открывает гугл таблицу статистики, начисляет балл и возвращает новое значение
def value_plus_one(j):
    gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
    sh = gc.open("bot_statistic")
    worksheet = sh.get_worksheet(0)
    worksheet.update(j, str(int(worksheet.acell(j).value) + 1))


# функция открывает гугл таблицу статистики и возвращает все значения в отсортированном виде
def pstat(cell):
    gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
    sh = gc.open("bot_statistic")
    worksheet = sh.get_worksheet(0)
    d1 = [(int(worksheet.acell(f'{cell}1').value), "Филч"), (int(worksheet.acell(f'{cell}2').value), "Игорь"),
          (int(worksheet.acell(f'{cell}3').value), "Серега"), (int(worksheet.acell(f'{cell}4').value), "Саня"),
          (int(worksheet.acell(f'{cell}5').value), "Леха(Саня)"), (int(worksheet.acell(f'{cell}6').value), "Леха(Фитиль)"),
          (int(worksheet.acell(f'{cell}7').value), "Диман"), (int(worksheet.acell(f'{cell}8').value), "Кирюха подкастер"),
          (int(worksheet.acell(f'{cell}9').value), "Женек спасатель"),
          (int(worksheet.acell(f'{cell}10').value), "Женек старый")]
    d1_sort = sorted(d1, reverse=True)
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
ему здоровья, успехов в личной жизни и новыйх побед.

/help - справка по боту''')


# функция обнуляющая все значения статистики в первый день нового месяца
def obnulenie_stat(bot):
    if datetime.now().day == 1:
        gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
        sh = gc.open("bot_statistic")
        worksheet = sh.get_worksheet(0)
        d1 = [(int(worksheet.acell('A1').value), "Филч"), (int(worksheet.acell('A2').value), "Игорь"),
              (int(worksheet.acell('A3').value), "Серега"), (int(worksheet.acell('A4').value), "Саня"),
              (int(worksheet.acell('A5').value), "Леха(Саня)"), (int(worksheet.acell('A6').value), "Леха(Фитиль)"),
              (int(worksheet.acell('A7').value), "Диман"), (int(worksheet.acell('A8').value), "Кирюха подкастер"),
              (int(worksheet.acell('A9').value), "Женек спасатель"), (int(worksheet.acell('A10').value), "Женек старый")]
        d1_sort = sorted(d1, reverse=True)
        cell = worksheet.find(d1_sort[0][1], in_column=2)
        worksheet.update(f'C{cell.row}', f'{int(worksheet.acell(f"C{cell.row}").value) + 1}')
        worksheet.update('A1:A10', [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])
        bot.send_message(group_id, f'''ИТОГИ МЕСЯЦА:

         1. {d1_sort[0][1]} -----> {d1_sort[0][0]} раз(а) 🎉🎉🎉 ЧЕМПИОН!!!
         2. {d1_sort[1][1]} -----> {d1_sort[1][0]} раз(а)
         3. {d1_sort[2][1]} -----> {d1_sort[2][0]} раз(а)
         4. {d1_sort[3][1]} -----> {d1_sort[3][0]} раз(а)
         5. {d1_sort[4][1]} -----> {d1_sort[4][0]} раз(а)
         6. {d1_sort[5][1]} -----> {d1_sort[5][0]} раз(а)
         7. {d1_sort[6][1]} -----> {d1_sort[6][0]} раз(а)
         8. {d1_sort[7][1]} -----> {d1_sort[7][0]} раз(а)
         9. {d1_sort[8][1]} -----> {d1_sort[8][0]} раз(а)
        10. {d1_sort[9][1]} -----> {d1_sort[9][0]} раз(а)

        Да здравствует наш чемпион месяца {d1_sort[0][1]}! В тяжелейшей борьбе он таки вырвал свою заслуженную победу.
        Пожелаем ему здоровья, успехов в личной жизни и новых побед.''')
    if datetime.now().day == 31 and datetime.now().month == 12:
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
        worksheet.update('A1:A10', [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])
        worksheet.update('C1:C10', [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])
        bot.send_message(group_id, f'''ИТОГИ ГОДА:

                 1. {d1_sort[0][1]} -----> {d1_sort[0][0]} раз(а) 🎉🎉🎉 ЧЕМПИОН!!!
                 2. {d1_sort[1][1]} -----> {d1_sort[1][0]} раз(а)
                 3. {d1_sort[2][1]} -----> {d1_sort[2][0]} раз(а)
                 4. {d1_sort[3][1]} -----> {d1_sort[3][0]} раз(а)
                 5. {d1_sort[4][1]} -----> {d1_sort[4][0]} раз(а)
                 6. {d1_sort[5][1]} -----> {d1_sort[5][0]} раз(а)
                 7. {d1_sort[6][1]} -----> {d1_sort[6][0]} раз(а)
                 8. {d1_sort[7][1]} -----> {d1_sort[7][0]} раз(а)
                 9. {d1_sort[8][1]} -----> {d1_sort[8][0]} раз(а)
                10. {d1_sort[9][1]} -----> {d1_sort[9][0]} раз(а)

                Да здравствует наш ПИДАРАС года {d1_sort[0][1]}! В тяжелейшей борьбе он таки вырвал свою заслуженную победу.
                Пожелаем ему здоровья, успехов в личной жизни и новых побед.''')
    else:
        pass


def celebrate_day():
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



# функция шара судьбы
def ball_of_fate():
    ball_choice = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    if ball_choice == 1:
        ball_answer = open("ball/var_one.png", 'rb')
        return ball_answer
    if ball_choice == 2:
        ball_answer = open("ball/var_two.png", 'rb')
        return ball_answer
    if ball_choice == 3:
        ball_answer = open("ball/var_tree.png", 'rb')
        return ball_answer
    if ball_choice == 4:
        ball_answer = open("ball/var_four.png", 'rb')
        return ball_answer
    if ball_choice == 5:
        ball_answer = open("ball/var_five.png", 'rb')
        return ball_answer
    if ball_choice == 6:
        ball_answer = open("ball/var_six.png", 'rb')
        return ball_answer
    if ball_choice == 7:
        ball_answer = open("ball/var_seven.png", 'rb')
        return ball_answer
    if ball_choice == 8:
        ball_answer = open("ball/var_eight.png", 'rb')
        return ball_answer
    if ball_choice == 9:
        ball_answer = open("ball/var_nine.png", 'rb')
        return ball_answer
    if ball_choice == 10:
        ball_answer = open("ball/var_ten.png", 'rb')
        return ball_answer
    if ball_choice == 11:
        ball_answer = open("ball/var_eleven.png", 'rb')
        return ball_answer


class Davinci:
    global saved_messages_davinci
    global provider_list

    def __init__(self, bot, message, text):
        try:
            self.bot = bot
            self.message = message
            self.text = text
            answer_davinci = open('davinci.txt.txt', 'r', encoding='utf-8')
            saved_messages_davinci.insert(0, f'Вы: {self.text}\n')
            prompt_davinci = (str(answer_davinci.read()) + ''.join(reversed(saved_messages_davinci)))
            self.bot.send_message(message.chat.id, f'секунду..')

            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_turbo,
                messages=[{"role": "user", "content": f'{prompt_davinci}'}],
                provider=choice(provider_list),
                stream=False)

            self.bot.send_message(message.chat.id, f'{response}')
            saved_messages_davinci.insert(0, f'{str(response)}\n')
            if len(saved_messages_davinci) >= 8:
                del saved_messages_davinci[3:]
        except Exception:
            self.bot.send_message(message.chat.id, "Простите но мне нужен перекур..")
            del saved_messages_davinci[1:]


class Artur:
    global saved_messages_artur
    global provider_list

    def __init__(self, bot, message, text):
        try:
            self.bot = bot
            self.message = message
            self.text = text
            answer_model = open('Artur.txt', 'r', encoding='utf-8')
            saved_messages_artur.insert(0, f'Вы: {self.text}\n')
            prompt_text = (str(answer_model.read()) + ''.join(reversed(saved_messages_artur)))
            self.bot.send_message(message.chat.id, f'секунду..')
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_turbo,
                messages=[{"role": "user", "content": f'{prompt_text}'}],
                provider=(choice(provider_list)),
                stream=False)
            self.bot.send_message(message.chat.id, f'{response}')
            saved_messages_artur.insert(0, f'{str(response)}\n')
            if len(saved_messages_artur) >= 6:
                del saved_messages_artur[3:]
        except Exception:
            self.bot.send_message(message.chat.id, "Занимайся..")
            del saved_messages_artur[1:]


def Artur_pozdravlyaet(bot, text):
    try:
        answer_model = open('Artur.txt', 'r', encoding='utf-8')
        saved_messages_artur.insert(0, f'Вы: {text}\n')
        prompt_text = (str(answer_model.read()) + ''.join(reversed(saved_messages_artur)))
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[{"role": "user", "content": f'{prompt_text}'}],
            provider=choice(provider_list),
            stream=False)
        bot.send_message(group_id, f'{response}')
        saved_messages_artur.insert(0, f'{str(response)}\n')
        if len(saved_messages_artur) >= 6:
            del saved_messages_artur[3:]
    except Exception:
        Artur_pozdravlyaet(bot, text)
        del saved_messages_artur[1:]
