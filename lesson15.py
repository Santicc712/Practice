# Как обрабатывать ошибки стр 93

# TRY

print("Введите -1 для выхода")
number = 1
while number != -1:
    try:
        number = int(input("Введите число: "))
        print("Вы ввели: ", number)
    except ValueError:
        print("Это было не число")
