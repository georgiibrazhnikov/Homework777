from hw311 import funk


def sdvig(a, k):
    c = len(a)
    m = a[(c-k):] + a[:(c-k)]
    return m
print("Введите список >> ")
a = funk()
k = int(input("Введите число k >> "))
print(sdvig(a, k))
assert sdvig([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert sdvig([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
assert sdvig([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
assert sdvig([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]