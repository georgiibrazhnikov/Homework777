from lister import funk


def binar(a, k):
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
    else:
        return s


print('Введите список >> ')
a = funk()
a.sort(key=int)
print(a)
k = int(input('Введите искомый элемент >> '))
print(binar(a, k))
assert binar([1, 2, 3, 4, 5, 6, 7], 5) == 4
assert binar([7, 22, 34, 41, 75, 69, 77], 7) == 0
assert binar([5, 2345, 33245, 42, 55, 634, 77], 1) == None
