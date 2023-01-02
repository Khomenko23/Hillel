"""
Задание 6:
Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort).
Вывести эти числа.
"""
A = []
a = int(input('Enter number N:'))
print('Now please add a set of N numbers for a list')
for i in range(a):
    b = int(input('Enter a number:'))
    i += 1
    A.append(b)
print(f'A list = {A}')

minimum = A[0]

for i in range(len(A)):
    if A[i] <= minimum:
        minimum = A[i]
        i += 1

maximum = A[0]

for i in range(len(A)):
    if A[i] >= maximum:
        maximum = A[i]
        i += 1

print(f'Minimum value from A list - {minimum}, maximum value - {maximum}')



