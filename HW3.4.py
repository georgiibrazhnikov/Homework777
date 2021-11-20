def funk():
    k = list()
    m = input()
    while m != "":
        k.append(m)
        m = input()
    return k
 
 
a = funk()
print("Элемент | Частота")
for i in set(a):
    b = k.count(i)
    print(i, "|", b)