from lister11 import funk


def binar(a, k):
    s = len(a) // 2
    e = len(a)
    b = 0
    while int(a[s - 1]) != k and b <= e:
        if k > int(a[s - 1]):
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