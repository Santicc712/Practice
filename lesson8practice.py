# password1 стр 67
# name = input("Как вас зовут? ")
# password = input("Какой пароль? ")
# if name == "Sandr" and password == "Usticci":
#    print("Welcome, Sandr")
# elif name == 'Santicc' and password == 'Qwer4455':
#    print("Welcome, Santicc")
# else:
#    print("Я вас не знаю")


# Угадайка Имя

print("Try to guess my name")
count = 1
name = "usticci"
guess = input("My name is? ")
while count < 3 and guess.lower() != name:
    print("Mistake")
    guess = input("My name is? ")
    count = count + 1

if guess.lower() != name:
    print("Mistake")
    print("U lose")
else:
    print("Yes! My name is", name + "!")
