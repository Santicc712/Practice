# Переменные с более чем одним значением. Контейнеры.

# Списки:
# months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
# 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
# Он состоит из элементов, которые нумеруются, начиная с О.
# Другими словами, если вам нужен январь, вы будете использовать months[0].
# Задайте списку номер, и он вернет значение, хранящееся в этом месте.


demolist = ['life', 52, 'Universal', 7, 'and', 12]  # Нумерация элементов с 0
print("demolist =", demolist)
demolist.append('all')  # Добавить элемент в список
print("после добавления 'all' demolist стал выглядеть так:")
print(demolist)
print("len(demolist) =", len(demolist))   # Узнать кол-во ячеек в списки
print("demolist.index(52) =", demolist.index(52))   # Узнать номер ячейки
print("demolist[1] =", demolist[1])   # Вытащить элемент по номеру ячейки

for c in range(len(demolist)):
    print("demolist[",c,"] =", demolist[c])

del demolist[2]
print('теперь список выглядит так:')
print(demolist)

if 'life' in demolist:
    print("'life' founded in list")
else:
    print("'life' not founded")

if 'omega' in demolist:
    print("'omgea' founded in list")
if 'omega' not in demolist:
    print("'omega' not founded")

another_list = [52, 7, 0, 69, 152]
another_list.sort()
print("Отсортированный список:", another_list)