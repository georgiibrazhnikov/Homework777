def nfact(a):
    if a < 2:
        return 1
    else:
        return a * nfact(a-1)


n = int(input("Введите n >> "))
print("n! = ", nfact(n))


def nfacttest():
    assert nfact(nfact(5) == 125), "Ошибка"

print