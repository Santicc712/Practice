# Файловый ввод/вывод стр 86

# Записать файл
with open('test.txt', "wt") as out_file:
    out_file.write("Этот текст отправляется в файл вывода\nПосмотрите на него "
                   "и увидите!")

# Чтение файла
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)

# Функция open(filename, mode)
# Filename имя файла, mode 'rt' чтение, 'wt" запись
# Функции read and write
# read - считывает следующую запись в файле и возвращает ее в виде строки
# Если аргумент не указан, она вернет весь файл
# write - добавляет строку в конец файла
