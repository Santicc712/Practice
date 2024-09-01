# RATE_TIMES Программа для вычисления скорости и расстояния

print("Введите скорость (rate) и расстояние (distance)")
rate = float(input("Скорость: "))
distance = float(input("Расстояние: "))
print("Время:", (distance / rate))

# Area Программа для вычисления периметра и площади прямоугольника

print("Вычислить информацию о прямоугольнике")
lenght = float(input("Длина: "))
width = float(input("Ширина: "))
print("Площадь:", lenght * width)
print("Периметр:", 2 * lenght + 2 * width)

# Temperature Шкала Фарингейта --> Цельсия

fahr_temp = float(input("Температура по Фарингейту: "))
print("Температура по Цельсию:", (fahr_temp - 32.0) * 5.0 / 9.0)

# Practice
string1 = input("Строка 1: ")
string2 = input("Строка 2: ")
float1 = float(input("Число 1: "))
float2 = float(input("Число 2: "))
print(string1 + string2)
print(float1 + float2)