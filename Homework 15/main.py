import collections
import random
from collections import Counter

"""
Задание 1
Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers
"""
numbers = []
f = open('text.txt', 'r')
file_data = f.read()
symbol = ''
for i in file_data:
    if i.isdigit():
        symbol += i
    elif symbol:
        numbers.append(int(symbol))
        symbol = ''
print(numbers)


"""
Задание 2 
Запросить у пользователя текст и записать его в файл data.txt 
"""
a = input('Please add some text: ')
file = open('data.txt', 'w')
file.write(a)

"""
Задание 3 
Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел
"""
random_numbers = ''
n = int(input('Please enter N number: '))
for i in range(n):
    num = input('Add a random number: ')
    random_numbers = random_numbers + num + ' '
    numbers = open('numbers.txt', 'w')
    numbers.write(random_numbers)



"""
Задание 4 
Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
"""
rand_values = ''
for i in range(100):
    a = str(random.randint(1, 1000))
    rand_values = rand_values + a + '\n'
    random_file = open('random_numbers.txt', 'w')
    random_file.writelines(rand_values)

"""
Задание 5 
Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
"""
words = 0
file = open('text.txt', 'r')
for line in file:
    words += len(line.split())

print("Words:", words)

"""
Задание 6 
Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
"""
suma = 0
file = open('file_with_numbers.txt', 'r')
f = file.read()
for i in f.split():
    if i.isdigit():
        suma = suma + int(i)
print(suma)

"""
Задание 7
Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
'в' - 20 раз
'привет' - 10 раз
'как' - 9 раз
'у' - 7
'world' - 4
"""
file = open('text.txt', 'r')
f = file.read()
words = f.split()
count = Counter(words).most_common(5)
print(count)

