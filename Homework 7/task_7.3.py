"""
Задание 3:
Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N
"""
A = []
for i in range(10):
    x = input('Enter a number:')
    i += 1
    A.append(x)
print(f'List A = {A}')

n = input('Enter N number:')
print(f'Number N is {A.count(n)} time(s) in a list A')
