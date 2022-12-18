"""
Вывести треугольник #3 с шириной N с помощью цикла while
"""
a = int(input('Enter N number:'))
i = 0
n = 0
while i < a:
    print(' '*n, end='')
    print('*'*a)
    a -= 1
    n += 1
