from hw311 import funk


def uniq(a):
    return len(set(a)) == len(a)


print("Введите список >> ")
a = funk()
print(uniq(a))
assert uniq([1, 2, 3, 4, 5]) == True
assert uniq([1, 2, 3, 4, 5, 5]) == False