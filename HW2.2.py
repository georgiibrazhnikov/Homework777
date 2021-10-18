spis = []
print('Введите целые положительные числа>>')
print('Введите <-1>, чтобы завершить ввод')
while True:
    x = int(input())
    if x == -1:
        break
    y = str(x)
    spis.append(y)
spis.sort(reverse = True)
print(''.join(spis))