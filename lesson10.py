# Использование модулей стр 74

# calendar.py
# import calendar
# year = int(input("Введите год: "))
# calendar.prcal(year)

# clock.py
# from time import time, ctime

# prev_time = " "
# while True:
#    the_time = ctime(time())
#    if prev_time != the_time:
#        print("Время: ", ctime(time()))
#        prev_time = the_time

# high_low.py

from random import randint
number = randint(0, 99)
guess = -1
while guess != number:
    guess = int(input("Угадайте число: "))
    if guess > number:
        print("Слишком много")
    elif guess < number:
        print("Слишком мало")
print("То, что нужно")
