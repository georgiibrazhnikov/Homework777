print('Введите a >>')
a = input()
print('Введите b >>')
b = input()
print('Введите c >>')
c = input()
print('Введите d >>')
d = input()
print('Введите f >>')
f = input()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
f = int(f)
k = f-d
if k == 0:
    print('Делить на ноль нельзя!')
else:
    g = (a * b - c) / k
    print(g)
