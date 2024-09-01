# Целое число (5) в строку => repr() == '5'

# Перевод строки "23" в целое число int("23") == 23

# Преобразование числа с плавающей точкой в строку
# 1.23 => repr(1.23) == '1.23'
# Преобразование чисел с плавающей точкой в целые
# 1.23 => int(1.23) == 1

# Перевод строки в число с плавающей точкой
# float("1.23") == 1.23
# float("123") == 123.0

# v = eval('123') # Возвращает тип данных, который мы ожидаем
# print(v, type(v))


# text = ("Это куча слов")
# print(text.split()) # Преобразует строку в список строк

# Нарезка строк

# text = "STRING"
# print(text[1:4]) TRI
# print(text[:5]) STRIN
# print(text[:-1]) STRIN
# print(text[-4:]) RING
# print(text[2]) R
# print(text[:]) STRING
# print(text[::-1]) GNIRTS

# Преобразует целое число в строку
def to_string(in_int):
    out_str = ""
    prefix = ""
    if in_int < 0:
        prefix = "-"
        in_int = -in_int
    while in_int // 10 != 0:
        out_str = str(in_int % 10) + out_str
        in_int = in_int // 10
    out_str = str(in_int % 10) + out_str
    return prefix + out_str


# Преобразует строку в целое число
def to_int(in_str):
    out_num = 0
    if in_str[0] == "-":
        multiplier = -1
        in_str = in_str[1:]
    else:
        multiplier = 1
    for c in in_str:
        out_num = out_num * 10 + int(c)
    return out_num * multiplier


print(to_string(2))
print(to_string(23445))
print(to_string(-23445))
print(to_int("14234"))
print(to_int("12345"))
print(to_int("-3512"))
