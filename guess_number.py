import random
rndnum = random.randint(1,101)
print('Попробуйте угадать число от 1 до 100))')
while True:
    gs = int(input("Введите число: "))
    if gs > rndnum:
        print("Ваше число больше того, что загадано")
    elif gs < rndnum:
        print("Ваше число меньше того, что загадано")
    else:
        break
print("Отличная интуиция! Вы угадали число :)")