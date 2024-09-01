# Fibonacci-method1 - программа вычисления последовательности Фибоначчи
# a = 0
# b = 1
# count = 0
# max_count = 20

# while count < max_count:
#   count = count + 1
#   print(a, end="  ") # аргумент end "" в функции print, не дает создавать новую строку
#   old_a = a # Отслеживает a с тех пор как мы его изменили
#   a = b
#   b = old_a + b
# print() # Получает новую пустую строку

# Fibonacci-method2 - упрощенный и ускоренный метод
# a = 0
# b = 1
# count = 0
# max_count = 10

# while count < max_count:
#    count = count + 1
#    print(a, b, end=" ") # Пробел в ковычках аргумента end меняет межстрочный интервал
#    a = a + b
#    b = a + b
# print()

# Fibonacci-method3
# a = 0
# b = 1
# count = 0
# max_count = 20

# Как только цикл запущен, мы остаемся в нем
# while count < max_count:
#    count += 1
#    olda = a
#    a = a + b
#    b = olda
#    print(olda, end=" ")
# print()

# Password - Ждет верного пароля, ctrl+c fast exit
# Цикл while исполняется, до тех пор пока не введен корректный пароль

# password = str()

# while password != 'usticci':
#    password = input("Пароль: ")
# print("Welcome")

# Login&Password prog Practice

login = input("Логин: ")
password = input("Пароль: ")
print("Чтобы заблокировать доступ, введите lock")
command = None
input1 = None
input2 = None
while command != "lock":
    command = input("Какая у вас комманда: ")
while input1 != login:
    input1 = input("Какое у вас имя пользователя: ")
while input2 != password:
    input2 = input("Какой у вас пароль: ")
print("Добро пожаловать")