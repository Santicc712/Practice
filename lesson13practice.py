# Phonebook

def print_numbers(numbers):
    print("Телефонные номера:")
    for k, v in numbers.items():
        print("Имя:", k, '\nНомер:', v)
    print()


def add_number(numbers, name, number):
    numbers[name] = number


def lookup_number(numbers, name):
    if name in numbers:
        return "Номер - " + numbers[name]
    else:
        return name + "Не найдено"


def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
    else:
        print(name, "Не найдено")


def load_numbers(numbers, filename):
    in_file = open(filename, "rt")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        in_line = in_line[:-1]
        name, number = in_line.split(",")
        numbers[name] = number
    in_file.close()


def save_numbers(numbers, filename):
    out_file = open(filename, 'wt')
    for k, v in numbers.items():
        out_file.write(k + "," + v + '\n')
    out_file.close()


def print_menu():
    print()
    print('1. Вывод телефонных номеров')
    print('2. Добавить номер телефона')
    print('3. Удалить номер телефона')
    print('4. Поиск телефонного номера')
    print('5. Загрузить номера')
    print('6. Сохранить номера')
    print('7. Выход')
    print()


phone_list = {}
menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Введите число (1-7): "))
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print("Добавить имя и номер")
        name = input("Имя: ")
        phone = input("Номер: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        print("Удалить имя и номер")
        name = input("Имя: ")
        remove_number(phone_list, name)
    elif menu_choice == 4:
        print("Поиск номера")
        name = input("Имя: ")
        print(lookup_number(phone_list, name))
    elif menu_choice == 5:
        filename = input("Имя файла для загрузки: ")
        load_numbers(phone_list, filename)
    elif menu_choice == 6:
        filename = input("Имя файла для сохранения: ")
        save_numbers(phone_list, filename)
    elif menu_choice == 7:
        break
    else:
        print_menu()

print("До свидания")
