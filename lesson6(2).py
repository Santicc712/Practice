menu_item = 0
namelist = []
while menu_item !=9:
    print("----------------")
    print("1. Вывод")
    print("2. Добавить элемент")
    print("3. Удалить элемент")
    print("4. Изменить элемент")
    print("9. Выйти")
    menu_item = int(input("Выберите пункт меню: "))
    if menu_item == 1:
        current = 0
        if len(namelist) > 0:
            while current < len(namelist):
                print(current, ".", namelist[current])
                current = current + 1
        else:
            print('Список пуст')
    elif menu_item == 2:
        name = input("Введите имя для добавления: ")
        namelist.append(name)
    elif menu_item == 3:
        del_name = input("Какой элемент вы хотите удалить: ")
        if del_name in namelist:
            item_number = namelist.index(del_name)
            del namelist[item_number]
        # namelist.remove(del_name) будет работать так же хорошо.
        # Код выше удаляет только первое вхождение
        # Ниже код удаляет все
        # while del_name in namelist:
        # item_number = namelist.index(del_name)
        # del namelist[item_number]
        else:
            print(del_name, 'not founded')
    elif menu_item == 4:
        old_name = input("Какое имя вы хотите изменить: ")
        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input("Введите новое имя: ")
            namelist[item_number] = new_name
        else:
            print(old_name, 'Not Founded')
print('Goodbye')
