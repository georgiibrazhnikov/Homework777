x = int(input())
y = int(input())
if x > 0 and y > 0:
        print('В первой четверти') 
elif x < 0 and y > 0:
        print('Во второй четверти')
elif x < 0 and y < 0:
        print('В третьей четверти') 
elif x > 0 and y < 0:
        print('В четвёртой четверти')
else: 
        print('На оси')
