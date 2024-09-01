#  Циклы for стр 58


# onetoten = range(1, 11) # Используем функцию range, которая включает в себя два аргумента
# for count in onetoten:
#    print(count)

# for count in range(1, 11): # Компактный вариант
#    print(count)

demolist = ['life', 52, 'Universal', 69, 'Qq']
for item in demolist:
    print(">>>> ", item)


list = [2, 52, 68, 7]
sum = 0
for num in list:
    sum = sum + num
    print("Сумма = ", sum)


dubllist = [4,52,52,52,68,5,3,4]
dubllist.sort()
prev = None
for item in dubllist:
    if prev == item:
        print("Дубликат", prev, "найден")
    prev = item


a = 1
b = 1
for c in range(1, 10):
    print(a, end=" ")
    n = a + b
    a = b
    b = n

# Все, что можно сделать с помощью циклов for,
# можно сделать и с помощью циклов while,
# но циклы for дают простой способ перебрать все элементы в списке
# или сделать что-то определенное количество раз.
