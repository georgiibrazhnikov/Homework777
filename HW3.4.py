print("Нажмите Enter")
from HW31 import funk
 

print("Введите список >> ")
a = funk()
print("Элемент | Частота")
for i in set(a):
    b = a.count(i)
    print(i, "|", b)