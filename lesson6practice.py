# Test prog

questions = [["Какого цвета дневное небо в ясный день?", "голубого"],
             ["Что является ответом на вопрос о жизни, Вселенной и всем остальном?", "52"],
             ["Какое слово из трех букв обозначает мышеловку?", "кот"],
             ["Какой звук издает по настоящему продвинутая машина?", "пинг"]]


def check_questions(questions_and_answer):
    question = questions_and_answer[0]
    answer = questions_and_answer[1]
    given_answer = input(question)
    if answer == given_answer:
        print("Nice!")
        return True
    else:
        print("Неверно, правильный ответ: ", answer)
        return False


def run_test(questions):
    if len(questions) == 0:
        print("Не было задано ни одного вопроса.")
        return
    index = 0
    right = 0
    while index < len(questions):
        if check_questions(questions[index]):
            right = right + 1
        index = index + 1
    print("Вы получили", right * 100 / len(questions),\
          "% правильно из", len(questions))


def show_questions():
    q = 0
    while q < len(questions):
        a = 0
        print("Q:", questions[q][a])
        a = 1
        print("A:", questions[q][a])
        q = q + 1


def menu():
    print("------------------")
    print("Menu:")
    print("1 - Пройти тест")
    print("2 - Просмотр списка вопросов и ответов")
    print("3 - Просмотр меню")
    print("5 - Выход")
    print("------------------")


choice = "4"
menu()
while choice != "5":
    choice = input("Выберите вариант из меню выше: ")
    if choice == "1":
        run_test(questions)
    elif choice == "2":
        show_questions()
    elif choice == "3":
        menu()
    elif choice == "5":
        print(" ", end="")
