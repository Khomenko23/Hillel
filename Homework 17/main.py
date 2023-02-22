"""
Необходимо создать класс Human с атрибутами:
name
surname
age
phone
address
Атрибуты должны заполняться в методе __init__

Так-же нужно написать методы:

get_info() - который возвращает словарь в котором находится информация о человеке
call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
Нужно создать 3 обьекта класса Human и вызвать у них метод get_info
"""


class Human:
    def __init__(self, name: str, surname: str, age: int, phone: str, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        print({f'Human info: {self.name}, {self.surname}, {self.age}, {self.phone}, {self.address}'})

    def call(self):
        print(f'{self.phone} вызывает абонента {phone_number}')


phone_number = '0501234567'

human_1 = Human('Kate', 'Brown', 20, '0578945612', 'Shevchenka 5')
human_2 = Human('Olena', 'Ivanova', 25, '0631234567', 'Soborna 36')
human_3 = Human('Viktoria', 'Melnyk', 23, '0671234567', 'Dovzhenka 7')

human_1.get_info()
human_2.get_info()
human_3.get_info()

human_1.call()

