from lister import funk


print('Введите список >> ')
a = funk()
print(a)
k = int(input('Введите искомый элемент >> '))


def binar(a, k):
    if not a:
        return None
    s = len(a) // 2
    e = len(a) - 1
    b = 0
    while int(a[s]) != k and b <= e:
        if k > int(a[s]):
            b = s + 1
        else:
            e = s - 1
        s = (b + e) // 2
    if b > e:
        return None
    for i in range(s+1):
        if a[i] == a[s] and i < s:
            s = i
        return s


print(binar(a, k))
assert binar([1, 2, 3, 4, 5, 6, 7], 5) == 4
assert binar([7, 22, 34, 41, 69, 75, 77], 7) == 0
assert binar([5, 42, 55, 77, 534, 645, 777], 1) is None
assert binar([], 1) is None
assert binar([7, 7, 7], 7) == 0
assert binar([], 42) is None
assert binar([0], 0) == 0
assert binar([0], 1) is None
assert binar([-1, 0, 42], 0) == 1
assert binar([-42, 0, 42], 42) == 2
assert binar([-6, -5, -4, -3, -2, -1], -4) == 2
assert binar([1, 2, 3, 4, 5, 6], 4) == 3
assert binar([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert binar([1, 2, 3, 4, 5], 7) is None
assert binar([1, 2, 3, 4, 5, 6], 7) is None
assert binar([42, 42, 42, 42, 42], 42) == 0
assert binar([-42, -42, -42, -42, -42], -42) == 0
assert binar([42, 42, 42, 42, 43], 43) == 4
assert binar([41, 42, 42, 42, 42], 41) == 0
assert binar([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
assert binar([-2, -2, -1, 0, 1, 1, 2, 2], 1) == 4