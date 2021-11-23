def nfact(a):
    if a < 2:
        return 1
    else:
        return a * nfact(a-1)


n = int(input("Введите n >> "))
print("n! = ", nfact(n))
assert nfact(5) == 120
assert nfact(7) == 5040
assert nfact(10) == 3628800