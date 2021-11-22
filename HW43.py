from HW311 import funk


def uniq():


    print("Введите список >> ")
    a = funk()
    if len(set(a)) == len(a):
        return True
    else:
        return False
print(uniq())


def uniqtest():
    assert uniqtest((len(set(a)) == len(a)) == False), "Ошибка"