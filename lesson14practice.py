# Продвинутое использование файлов txt стр 90


assignments = ['hw ch 1', 'hw ch 2', 'quiz ', 'hw ch 3', 'test']
students = { }


def load_grades(gradesfile):
    inputfile = open(gradesfile, 'r')
    grades = []
    while True:
        student_and_grade = inputfile.readline()
        student_and_grade = student_and_grade[:-1]
        if not student_and_grade:
            break
        else:
            studentname, studentgrades = student_and_grade.split(",")
            studentgrades = studentgrades.split(" ")
            students[studentname] = studentgrades
    inputfile.close()
    print("Оценки загружены")


def save_grades(gradesfile):
    outputfile = open(gradesfile, 'w')
    for k, v in students.items():
        outputfile.write(k + ",")
        for x in v:
            outputfile.write(str(x) + " ")
        outputfile.write("\n")
    outputfile.close()
    print("Оценки сохранены")


def print_menu():
    print("1. Добавить студента")
    print("2. Удалить студента")
    print("3. Загрузить оценки")
    print("4. Записать оценку")
    print("5. Распечатать оценки")
    print("6. Сохранить оценки")
    print("7. Меню печати")
    print("9. Выход")


def print_all_grades():
    if students:
        keys = sorted(students.keys())
        print('\t', end=' ')
        for x in assignments:
            print(x, '\t', end=' ')
        print()
        for x in keys:
            print(x, '\t', end=' ')
            grades = students[x]
            print_grades(grades)
    else:
        print("Нет оценок для печати")


def print_grades(grades):
    for x in grades:
        print(x, '\t', end=' ')
    print()


print_menu()
menu_choice = 0
while menu_choice != 9:
    print()
    menu_choice = int(input("Выбор меню: "))
    if menu_choice == 1:
        name = input("Студент, которого нужно добавить: ")
        students[name] = [0] * len(assignments)
    elif menu_choice == 2:
        name = input("Студент, которого нужно удалить: ")
        if name in students:
            del students[name]
        else:
            print("Студент:", name, 'не найден')
    elif menu_choice == 3:
        gradesfile = input("Загрузить оценки из какого файла? ")
        load_grades(gradesfile)
    elif menu_choice == 4:
        print("Записать оценку")
        name = input("Студент: ")
        if name in students:
            grades = students[name]
            print('Введите число оценки для записи')
            print("Введите 0 для выхода")
            for i,x in enumerate(assignments):
                print(i + 1, x, '\t', end=' ')
            print()
            print_grades(grades)
            which = 1234
            while which != -1:
                which = int(input("Изменить какую оценку: "))
                which -= 1
                if 0 <= which < len(grades):
                    grade = input("Grade: ")
                    grades[which] = grade
                elif which != -1:
                    print("Неверная цифра оценки")
        else:
            print("Студент не найден")
    elif menu_choice == 5:
        print_all_grades()
    elif menu_choice == 6:
        gradesfile = input("Сохранить оценки в какой файл? ")
        save_grades(gradesfile)
    elif menu_choice != 9:
        print_menu()