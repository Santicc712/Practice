# Example == how work
# with numbers
# print(5 == 6)
# with Переменные
# x = 5
# y = 12
# print(x == y)

###########################################

# High_low example game code Угадайка

# number = 7
# guess = 1

# print("Try to guess number")
# while guess != number:
#    guess = int(input("Number: "))

#    if guess == number:
#        print("Wow u so lucky!")
#    elif guess < number:
#        print("Try one more: ")
#    elif guess > number:
#        print("Not that big")

#########################################

# Even example code Чет/Нечет

# number = float(input("Назовите число "))
# if number % 2 == 0:
#    print(int(number), "- четное")
# elif number % 2 == 1:
#    print(int(number), "- нечетное")
# else:
#    print(number, "- очень странно")

###########################################

# Average1 Выводит среднее значение, продолжает работу пока не будет введено 0

# count = 0
# sum = 0.0
# number = 1  # Установить значение, которое не приведет к завершению цикла while

# print("Введите 0, чтобы выйти из цикла")

# while number != 0:
#    number = float(input("Введите число: "))
#    if number != 0:
#        count = count + 1
#        sum = sum + number
#    if number == 0:
#        print("Среднее значение составило: ", sum / count)


# Average2 Выводит среднее значение, запрашивает числа пока не будут введены все числа

# sum = 0.0
# print("Эта программа возьмет несколько чисел и усреднит их")
# count = int(input("Сколько чисел вы хотите усреднить: "))
# current_count = 0

# while current_count < count:
#    current_count = current_count + 1
#    print("Число", current_count)
#    number = float(input("Введите число: "))
#    sum = sum + number

# print("Среднее значение составило: ", sum / count)

# Code описание имен

# name = input("Ваше имя: ")
# if name == "Santicc":
#    print("U have nice name")
# elif name == "Vlad":
#    print("Suck dick, Vladik")
# elif name == "Gena":
#    print("Stupid ass whore")
# else:
#    print("Cool name, bro")

# Модифицировать Угадайку

# number = 7
# guess = -1
# count = 0

# print("Try to guess number")
# while guess != number:
#    guess = int(input("Number: "))
#    count = count + 1
#    if guess == number:
#       print("Wow u so lucky!")
#    elif guess < number:
#        print("Try one more: ")
#    elif guess > number:
#        print("Not that big")

# if count > 3:
#    print("It's so hard for u")
# else:
#    print("Good Job!")


# Big number code
number1 = float(input("Введите число 1: "))
number2 = float(input("Введите число 2: "))
if number1 + number2 > 100:
    print("BIG NUMBER")
