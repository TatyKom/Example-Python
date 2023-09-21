import random


def num():
    while True:
        try:
            n = int(input())
            if 0 < n:
                return n
            else:
                print("Неправильный ввод. Введите целое положительное число.")
        except ValueError:
            print("Неправильный ввод. Введите целое число")


gamer1, gamer2 = input("Как Вас зовут?").split()
random_number = random.randint(4, 50)
print("Уважаемые ", gamer1, " и ", gamer2, " ! Перед вами случайное натуральное число ", random_number)
random_gamer = random.randint(0, 1)
print("Введите любой из делителей имеющегося числа."
      "Делитель вычитается из натурального числа. Проигрывает тот, кто получит ноль.")
while random_number > 0:
    if random_gamer == 0:
        print(gamer1, " Ваш ход. Ввведите любой делитель имеющегося числа.")
    if random_gamer == 1:
        print(gamer2, " Ваш ход. Ввведите любой делитель имеющегося числа.")
    divider = num()
    if not random_number % divider == 0:
        print("Вы ввели не делитель. Повторите ввод")
        divider = num()
    random_number -= divider
    print("Осталось число ", random_number)
    if random_number == 0:
        if random_gamer == 0:
            print("Игра закончена. Выиграл ", gamer2)
        else:
            print("Игра закончена. Выиграл ", gamer1)
            break
    random_gamer = 1 - random_gamer