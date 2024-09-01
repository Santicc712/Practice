# Temperature 2 перевод в градусы Фаренгейта / Цельсия

# def print_options():
#    print("Опции: ")
#    print(" 'm' Меню ")
#    print(" 'f' Конвертировать в Фаренгейта ")
#    print(" 'c' Конвертировать в Цельсия ")
#    print(" 'q' Выйти ")


# def cel_to_far(c_temp):
#    return 9.0 / 5.0 * c_temp + 32


# def far_to_cel(f_temp):
#    return (f_temp - 32.0) * 5.0 / 9.0


# choice = 'm'
# while choice != "q":
#    if choice == "f":
#        c_temp = float(input("Температура по Цельсию: "))
#        print("Фаренгейт: ", cel_to_far(c_temp))
#        choice = input("option: ")
#    elif choice == "c":
#        f_temp = float(input("Температура по Фарингейту: "))
#        print("Цельсий:", far_to_cel(f_temp))
#        choice = input("option: ")
#    elif choice == "m":

#        print_options()
#        choice = input("option: ")


# Area2 Вычисляет площадь прямоугольника


def welcome(name):
    print("Добро пожаловать!", name)
    print("Эта программа вычислит площадь квадрата\n"
          "круга или прямоугольника")


def rectangle(width, height):
    return width * height


def square(L):
    return L * L


def circle(radius):
    return 3.14159 * radius ** 2


name = input('Ваше имя: ')
welcome(name)


def options():
    print()
    print("Опции:")
    print(" 's' Площадь квадрата ")
    print(" 'c' Площадь круга ")
    print(" 'r' Площадь прямоугольника ")
    print(" 'q' Выйти ")
    print()


choice = 'x'
options()
while choice != "q":
    choice = input("Пожалуйста, введите ваш выбор: ")
    if choice == 's':
        L = float(input("Длина стороны квадрата: "))
        print("Площадь квадрата равна", square(L))
        options()
    elif choice == "c":
        radius = float(input("Радиус круга: "))
        print("Площадь круга равна", circle(radius))
        options()
    elif choice == "r":
        width = float(input("Ширина прямоугольника: "))
        height = float(input("Высота прямоугольника: "))
        print("Площадь прямоугольника равна ", rectangle(width, height))
        options()
    elif choice == "q":
        print(" ", end="")
    else:
        print("Неизвестная команда.")
        options()

