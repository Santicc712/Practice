# Месть строк стр 81
def shout(string):
    for character in string:
        print("Дайте мне " + character)
        print("'" + character + "'")

shout("Lose")


def middle(string):
    print("Средний символ:", string[len(string) // 2])


middle("abcdefg")
middle("The Python Programming Language")
middle("Atlanta")

# Эти программы демонстрируют схожесть строк и списков
# Большинство функций списков работает и со строками


## Преобразование строки в верхний регистр


def to_upper(string):
    upper_case = ""
    for character in string:
        if 'a' <= character <= 'z':
            location = ord(character) - ord('a')
            new_ascii = location + ord('A')
            character = chr(new_ascii)
        upper_case = upper_case + character
    return upper_case


upper = to_upper("text")
print(upper)
