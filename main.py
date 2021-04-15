import telebot;
bot = telebot.Telebot(1786018024:AAFmf6Y5AJbGGpHnrR9IZ1tagxTinrC0GAY)

#модуль случайных чисел 
import random

#заголовок для первого предложения
first = ["Сегодня идеальный день для новых начинаний.","Оптимальный день, чтобы решиться на смелый поступок!"]
second = ["Но, помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про"]
second_add = ["отношения с друзьями и близкими","работу и деловые вопросы, которые могут так некстати помешать планам."]
third = ["Злые языки могут наговорить Вам обратное, но сегодня их слушать не нужно","Знайте, что успех благоволит лишь настойчивым"]

#выводим знаки зодиака
print("1 - Овен")
print("2 -Телец")
print("3 -Близнецы")
print("4 -Рак")
print("5 -Лев")
print("6 -Дева")
print("7 -Весы")
print("8 -Скорпион")
print("9 -Стрелец")
print("10 - Козерог")
print("11 - Водолей")
print("12 - Рыбы")

#спрашиваем у пользователя его знак
zodiac = int(input("{blue}Введите число с номеро знака зодиака: {endcolor}".format(blue="\033[96m", endcolor="\033[0m")))
if 0 < zodiac < 13:
    print(ranom.choice(first), random.choice(second), random.choice(second_add), random.choice(third))
else:
    print("Вы ввели не то число, запустите программу еще раз")

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу случайныйй гороскоп")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю! Напиши /help")

bot.polling(none_stop=True, interval=0)
