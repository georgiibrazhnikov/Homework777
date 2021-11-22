def sdvig():
    from HW311 import funk


    k = int(input("Введите число k >> "))
    print("k = ", k)
    print("Введите список >> ")
    a = funk()
    c = len(a)
    m = a[(c-k):] + a[:(c-k)]
    return m 
print(sdvig())


def sdvigtest():
    assert sdvigtest(2,[1, 2, 3, 4, 5] == [4, 5, 1, 2, 3]), "Ошибка"
    assert sdvigtest(3,[1, 2, 3, 4, 5] == [3, 4, 5, 1, 2]), "Ошибка"
    assert sdvigtest(0,[1, 2, 3, 4, 5] == [1, 2, 3, 4, 5]), "Ошибка"
    assert sdvigtest(7,[1, 2, 3, 4, 5] == [4, 5, 1, 2, 3]), "Ошибка"