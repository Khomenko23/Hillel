a = int(input('Enter N number:'))
if a % 2 == 1 and a > 20:
    print('Not Weird')
elif a % 2 == 0 and 2 <= a <= 5:
    print('Not Weird')
elif a % 2 == 0 and 6 <= a <= 20:
    print('Weird')
elif a % 2 == 1:
    print('Weird')
else:
    print('Data is invalid')

