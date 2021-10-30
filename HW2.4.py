v = input()
x = v.count('(')
y = v.count(')')
z = x - y
if z > 0:
    print('Не хватает закрывающих:', z)
elif z < 0:
    print('Не хватает открывающих:', -z)
else:
    print('Ошибок нет')