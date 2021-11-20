def arifm(n):
    if len(n) == 0:
        return 0
    else:
        return sum(n) / len(n)


spis = list()
a = input("Введите последовательность чисел >> ")
while a != "":
    spis.append(int(a))
    a = input()
print(arifm(spis))