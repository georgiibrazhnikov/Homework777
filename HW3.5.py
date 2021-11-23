from hw31 import funk


def arifm(n):
    if len(n) == 0:
        return "Ошибка"
    else:
        return sum(n) / len(n)


spis = list()
print("Введите последовательность чисел >> ")
a = funk()
for x in a:
    if x != " ":
        spis.append(int(x))
    else:
        break
print(arifm(spis))