max_points = [25, 25, 52, 25, 100]
assignments = ['hw ch 1', 'hw ch 2', 'quiz   ', 'hw ch 3', 'test']
students = {'#Max': max_points}


# Первые две строки просто создают два списка.
# Следующая строка students = {'#Мах': max_points} создает новый словарь
# с ключом {#Мах} и значением [25, 25, 50, 25, 100]
# Далее определяется print_menu.
# Затем определяется функция print_all_grades в строках


def print_menu():
    print('1. Добавить студента')
    print('2. Удалить студента')
    print('3. Вывести оценки')
    print('4. Записать оценку')
    print('5. Меню вывода')
    print('6. Exit')


def print_all_grades():
    print('\t', end=' ')
    for i in range(len(assignments)):
        print(assignments[i], '\t', end=' ')
    print()
    keys = list(students.keys())  # ключи извлекаются из словаря  # keys - итерируемая переменная, и она преобразуется в список
    keys.sort()  # Ключи сортируются
    for x in keys: # Используем для перебора всех ключей
        print(x, '\t', end=' ')
        grades = students[x]  # Дает оценкам список, хранящийся по ключу x
        print_grades(grades)  # Функция Выводит список, определена несколькими страками ниже


def print_grades(grades):
    for i in range(len(grades)):
        print(grades[i], '\t', end=' ')
    print()


print_menu()
menu_choice = 0
while menu_choice != 6:
    print()
    menu_choice = int(input("Введите число (1-6): "))
    if menu_choice == 1:
        name = input("Студент для добавления: ")
        students[name] = [0] * len(max_points)  # Добавляет студента к ключу его имени
    elif menu_choice == 2:
        name = input("Студент, которого нужно удалить: ")
        if name in students:
            del students[name]
        else:
            print("Студент:", name, "не найден")
    elif menu_choice == 3:
        print_all_grades()
    elif menu_choice == 4:
        print("Записать оценку")
        name = input("Студент: ")
        if name in students:
            grades = students[name]  # Извлечение оценок, получает ссылку на оценки имени студента
            print("Введите оценку для записи")
            print("Введите 0 (ноль) для выхода")
            for i in range(len(assignments)):
                print(i + 1, assignments[i], '\t', end=' ')
            print()
            print_grades(grades)
            which = 1234
            while which != -1:
                which = int(input("Изменить оценку: "))
                which -= 1
                if 0 <= which < len(grades):
                    grade = int(input("Оценка: "))
                    grades[which] = grade  # Здесь оценка записывается
                elif which != -1:
                    print("Неверное число оценки")
            else:
                print("Студент не найден")
    elif menu_choice != 6:
        print_menu()


# Словари предоставляют простой способ связать ключи со значениями.
# Их можно использовать для удобного отслеживания данных,
# которые привязаны к различным ключам.
