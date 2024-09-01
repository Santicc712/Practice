# Словари стр 68

def print_menu():
    print()
    print('1. Вывод телефонных номеров')
    print('2. Добавить номер телефона')
    print('3. Удалить номер телефона')
    print('4. Поиск телефонного номера')
    print('5. Exit')
    print()


numbers = {}  # Создаем словарь
menu_choice = 0
print_menu()
while menu_choice !=5:
    menu_choice = int(input("Введите число (1-5): "))
    if menu_choice == 1:
        print("Phone numbers: ")
        for x in numbers.keys():  # функция numbers.keys() возвращает список
            print("Имя: ", x, "\tНомер:", numbers[x])  # просматривают словарь и выводят всю информацию
        print()
    elif menu_choice == 2:
        print("Add name and phone")
        name = input("Name: ")
        phone = input("Phone: ")
        numbers[name] = phone  # Добавляет в словарь имя и номер телефона, не учитывает повторение имен
    elif menu_choice == 3:
        print("Delete name and phone")
        name = input("Name: ")
        if name in numbers:  # Проверяет есть ли имя в словаре и удаляет, если есть
            del numbers[name]  # Удаляет ключ name и значение, связанное с этим ключом
        else:
            print(name, 'Not found')
    elif menu_choice == 4:
        print("Search phone")
        name = input("Name: ")
        if name in numbers:  # Проверка есть ли в словаре определенный ключ, если есть, выводит связанный с ним номер
            print("Номер: ", numbers[name])
        else:
            print(name, "not found")
    elif menu_choice != 5:
        print_menu()


# Вкратце: в словарях есть ключи и значения.
# Ключи могут быть строками или числами и указывают на значения.
# Значениями могут быть переменные любого типа (включая списки и даже словари)


# Пример использования списка в словаре: IN LESSON9(2)
