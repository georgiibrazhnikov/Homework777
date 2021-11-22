def nfact(a):
    if a < 2:
        return 1
    else:
        return a * nfact(a-1)


n = int(input("Введите n >> "))
print("n! = ", nfact(n))


def sdvigtest():
    assert nfacttest(nfact(5) == 125), "Ошибка"