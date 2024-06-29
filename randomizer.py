print(
    "Привет, манюня! Здесь тебе нужно угадать число от 1 до 100(вклчительно).",
    "Введи его в консоль:",
)
from random import *


def randomizer(number):
    num1 = randint(1, 100)
    cnt = 0
    while True:
        if number == num1:
            print(
                f"Поздравляю, моя любимая Катя Старшая! Ты победила за {cnt} шагов! Это очень хавофый результат!"
            )
            print('Моя любовь хочет сыграть ещё раз? напиши "ни" или "дя":')
            katya = input()
            if katya == "дя":
                cnt = 1
                num1 = randint(1, 100)
                print("Тифоня, пишите новое число:")
                x = int(input())
                continue
            elif katya == "ни":
                return
        elif number >= num1:
            print("Число больше загаданного, попробуй ещё раз)")
            cnt += 1
            number = int(input())
            continue
        elif number <= num1:
            print("Число меньше загаданного, попробуй ещё раз)")
            cnt += 1
            number = int(input())
            continue


x = int(input())
randomizer(x)
