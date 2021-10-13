print('Введите X, Y>>')
x = int(input())
y = int(input())
s = 0
for i in range(x, y):
    if i % 5 == 0:
        s = s+1
print(s)
