def vrgod(month):
    if 9 <= month <= 11:
        vrgod = "Осень"
    elif 3 <= month <= 5:
        vrgod = "Весна"
    elif 6 <= month <= 8:
        vrgod = "Лето"
    elif 1 <= month <= 2 or month == 12:
        vrgod = "Зима"
    else:
        print("Нет такого месяца")
    return vrgod


n  = int(input("Введите номер месяца >> "))
print(vrgod(n))