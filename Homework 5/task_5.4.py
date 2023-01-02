"""
Вывести треугольник #4 с шириной N с помощью цикла while
"""
a = int(input('Enter N number:'))
i = 0
n = 0
while i <= a:
    print(' '*a, end='')
    print('*'*n)
    a -= 1
    n += 1
