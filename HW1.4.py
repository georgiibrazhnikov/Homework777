print('Введите слово>>')
s = input()
p = s[::-1]
print(p)
if s == p:
    print('Это палиндром.')
else:
    print('Это не палиндром.')