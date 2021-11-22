from hw311 import funk


def uniq():
    return len(set(a)) == len(a)


print("Введите список >> ")
a = funk()
print(uniq())


def uniqtest():
    assert uniqtest((len(set(a)) == len(a)) == False), "Ошибка"


print(uniqtest(uniq))