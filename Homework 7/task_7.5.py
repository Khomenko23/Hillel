"""
Задание 5:
Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C
"""
A = []
C = []
i = 0
for char in range(5):
    x = int(input('Enter a number for A list:'))
    char += 1
    A.append(x)
print(f'A list = {A}')
for A[i] in A:
    if A[i] >= 5:
        C.append(A[i])
        i += 1
print(f'New C list = {C}')





