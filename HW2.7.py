from random import randint

k = randint(0, 100)
print('Загадайте число от 0 до 100 >>')
x = int(input())
while k != x:
    print('Вы не угадали :(')
    if k > x:
        print('Загаданное число больше!')
    elif k < x:
        print('Загаданное число меньше!')
    x = int(input())
print('Вы угадали число!')
