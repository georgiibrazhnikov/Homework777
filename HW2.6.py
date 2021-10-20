print('Введите строку >>')
l = list(input())
a = []
for i in l:
    if i.isdigit():
        a.append(i)
print('Введите k >>')
k = int(input())
print(k, '-ая цифра в строке', a[k-1])
