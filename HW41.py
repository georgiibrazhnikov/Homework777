from hw311 import funk


def sdvig():
    k = int(input("Введите число k >> "))
    print("k = ", k)
    print("Введите список >> ")
    a = funk()
    c = len(a)
    m = a[(c-k):] + a[:(c-k)]
    return m 
print(sdvig())


def sdvigtest():
    assert sdvig(2,[1, 2, 3, 4, 5] == [4, 5, 1, 2, 3]), "Ошибка"
    assert sdvig(3,[1, 2, 3, 4, 5] == [3, 4, 5, 1, 2]), "Ошибка"
    assert sdvig(0,[1, 2, 3, 4, 5] == [1, 2, 3, 4, 5]), "Ошибка"
    assert sdvig(7,[1, 2, 3, 4, 5] == [4, 5, 1, 2, 3]), "Ошибка"


print(sdvigtest(sdvig))