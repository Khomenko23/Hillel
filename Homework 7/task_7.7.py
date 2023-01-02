"""
Задание 7:
Пользователь вводит текст нужно вывести количество цифр в этом тексте
"""
digits = 0
text = input('Please enter a short sentence with numbers in it:')
for i in text:
    if i.isdigit():
        digits += 1

print(f'The total number of digits in your sentence is {digits}')

