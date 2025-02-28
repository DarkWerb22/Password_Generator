from string import printable
from random import choice


symbols = list(printable[:-6])
status = False
while True:
    length = int(input("Выберете длинну пароля от 7 до 20: "))
    if length < 7 or length > 20:
        print("Пароль слишком длинный, Попробуйте еще раз")
    else:
        break

while not status:
    password = "".join(choice(symbols) for _ in range(length))
    print("Пароль:", password)
    answer = input("Вам нравится ваш пароль? ")
    if answer.lower() == "да":
        status = True
        print("Отлично вот ваш новый пароль: ", password)
    elif answer.lower() == "нет":
        continue
    else:
        print("Система не понимает вашего ответа")
        break
