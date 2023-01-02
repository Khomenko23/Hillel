"""
Задание 4:
Запросить у пользователя число N
Запросить у пользователя N чисел и записать их в список A
Вывести список в обратной последовательности"
"""
A = []
a = int(input('Enter number N:'))
print('Now please add a set of N numbers for a list')
for i in range(a):
    b = int(input('Enter a number:'))
    i += 1
    A.append(b)
A.reverse()
print(A)

