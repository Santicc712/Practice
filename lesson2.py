print("Стой!")
user_input = input("Кто идет?") # Это переменная, в них можно хранить некоторые данные
print("Вы можете пройти", user_input)

#######################################################

#Примеры переменных
a = 69.69
b23 = 'Spamchik'
first_name = "Sancho"
b = 712
c = a+b
print("a + b равно", c)
print('Имя - ', first_name)
print('Sorted Parts, After midnight or', b23)

#Переменными приведенными выше являются a, b23, first_name, b, c
#Два основных типа переменных -- СТРОКИ и ЧИСЛА
# СТРОКИ ОКРУЖЕНЫ "" / ''

########################################################

#ПРИМЕР
number = float(input("Введите число: "))
integer = int(input("Введите целое число: "))
text = input("Введите строку: ")
print("число =", number)
print("число - это", type(number))
print("число * 2 =", number * 2)
print("целое число =", integer)
print("целое число - это", type(integer))
print("целое число * 2 =", integer * 2)
print("текст =", text)
print("текст - это", type(text))
print("текст * 2 =", text * 2)

##############################################

# Обратите внимание, что число было создано с помощью float ( input ()),а текст - с помощью input().
# input() возвращает строку, а функция float возвращает число из строки.
# int возвращает целое число, то есть число без десятичной точки.
# Если вы хотите, чтобы пользователь ввел десятичную дробь, используйте float(input() ),
# если вы хотите, чтобы пользователь ввел целое число, используйте int(input() ),
# а если вы хотите, чтобыпользователь ввел строку, используйте input ().

##############################################

# Во второй половине программы используется функция type()
# которая сообщает, к какому типу относится переменная.
# Числа имеют тип int или float, что является сокращением от integer и Floating point
# Текстовые строки имеют тип str, сокращение от string.

##############################################

# Взаимодействие со строками
# Повторение *  print("i" * 5) == "iiiii"
# Соединение +  print("Hello" + "World") =="Hello World"