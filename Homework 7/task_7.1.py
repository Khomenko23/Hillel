"""
Задание 1:
Запросить у пользователя 5 чисел и записать их в список
"""
list = []
for i in range(5):
    x = int(input('Enter a number:'))
    i += 1
    list.append(x)
print(f'List = {list}')