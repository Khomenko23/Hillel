"""Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.

Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
в котором каждый элемент списка является и ключом и значением.
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

Напишите функцию sum_range(start, end),
которая суммирует все целые числа от значения «start» до величины «end» включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами."""


def change(lst):
    new_first = lst.pop()
    new_last = lst.pop(0)
    lst.append(new_last)
    lst.insert(0, new_first)
    return lst


print(change([1, 2, 3, 4]))


def to_dict(lst):
    return {element: element for element in lst}


print(to_dict([1, 2, 3, 4]))


def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end+1))


print(sum_range(1, 10))
