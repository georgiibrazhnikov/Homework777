def funk(n):
    x = 0
    y = 1
    if n < 1:
        print("Ошибка")
    print(x , y)
    for i in range(n-2):
        x += y
        print(x)
        x , y = y, x 


m = funk(int(input("Введите число >> ")))
