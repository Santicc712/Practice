# Подробнее о списках

# some_numbers = ['ноль', 'один' 'два' 'три' 'четыре' 'пять']
# some_numbers[0] индекс 0 выведет 'ноль' из списка
# some_numbers[-1] индекс -1 выведет 'пять' из списка
# some_numbers[0:3] нарезка выведет 'ноль' 'один' 'два'
# some_numbers[:2] такой способ выведет 'ноль' 'один'
# some_numbers[-2:] выведет 'четыре' 'пять'

# poem = [
#    "<В>", "Jack", "and", "Jill", "</В>", "went", "up", "the", "hill", "to", "<В>", "fetch", "а", "pail", "of",
#    "</В>", "water.", "Jack", "fell", "<В>", "down", "and", "broke", "</В>", "his", "crown", "and", "<В>", "Jill", "came",
#    "</В>", "tumbling", "after"
# ]


# def get_bolds(text):
#    is_bold = False
#    start_block = 0
#    bold_fragments = []

#    for index in range(len(text)):
#        if text[index] == "<В>":
#            if is_bold:
#                print("Error: Extra Bold")
#                continue
#            is_bold = True
#            start_block = index + 1

#        elif text[index] == "</В>":
#            if not is_bold:
#                print("Error: Extra Close Bold")
#                continue
#            bold_fragments.append((start_block, index, text[start_block:index]))
#            is_bold = False

#    if is_bold:
#        print("Error: Unmatched Bold Tag")

#    return bold_fragments


# bolds = get_bolds(poem)
# print(bolds)

# Копирование
# a = [1, 2, 3]
# b = a
# print(b)

# b[1] = 10
# print(b)
# print(a)

# Изменение b привело к изменению а.
# Дело в том, что оператор b = а делает b ссылкой на а

# Однако некоторые присваивания не создают двух имен
# для одного списка:
# a = [1, 2, 3]
# b = a * 2
# print(a)
# print(b)
# a[1] = 10
# print(a)
# print(b)

# В этом случае b не является ссылкой на a,
# поскольку выражение a * 2 создает новый список.
# Оператор b = а * 2 дает b ссылку на a * 2, а не ссылку на а.
# Все операции присваивания создают ссылку

# Способы создания копии списка
# a = [1, 2, 3]
# b = a[:]
# b[1] = 10
# print(a)
# print(b)

# Использование нарезки [:] создает новую копию списка.
# Однако этим способом копируется только внешний список.

import copy
a = [[1, 2, 3], [4, 5, 6]]
b = a[:]
c = copy.deepcopy(a)
b[0][1] = 10
c[1][1] = 12
print(a)
print(b)
print(c)
