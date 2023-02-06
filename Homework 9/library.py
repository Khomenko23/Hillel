from typing import Union

number_request = 'Please enter a number like 1.00 or 10 >>> '


def get_coins(number: int) -> str:
    last_digit = int(str(number)[-1])

    if number == 0 or number in range(5, 21) or last_digit == 0:
        result = 'копійок'
    elif number == 1 or last_digit == 1:
        result = 'копійка'
    elif number in [2, 3, 4] or last_digit in [2, 3, 4]:
        result = 'копійки'

    return result


def get_hryvnas(number: int) -> str:
    last_value = int(str(number)[-1])

    if number == 0 or number in range(5, 21) or last_value in [5, 10]:
        result = 'гривень'
    elif number == 1 or last_value == 1:
        result = 'гривня'
    elif number in [2, 3, 4] or last_value in [2, 3, 4]:
        result = 'гривні'

    return result


def get_number(number: Union[int, float]) -> list:
    result = []
    received_number = str(float(number))
    list_number = received_number.split('.')
    hryvnas = int(list_number[0])
    if len(list_number[1]) == 1:
        coins = int(list_number[1]) * 10
    elif len(list_number[1]) > 2:
        coins = int(list_number[1][:2])
    else:
        coins = int(list_number[1])
    received_hryvnas = get_hryvnas(hryvnas)
    received_coins = get_coins(coins)
    result.append(f'{hryvnas} {received_hryvnas}')
    result.append(f'{coins} {received_coins}')

    return result


def is_hot_today(temp: Union[int, float]) -> bool:
    if temp >= 25:
        result = True
    else:
        result = False

    return result


lmd_list = [lambda temp: True if (temp >= 25) else False, 2]


def get_user_number(message: str = number_request, need_int=False) -> Union[int, float]:
    while True:
        received_value = input(message)
        try:
            result = float(received_value)
            if need_int:
                return int(result)
            return result

        except ValueError:
            print('\nYour number is not appropriate. Try again')


def logic_value(need_positive: bool = True):
    if need_positive:
        return lambda x: abs(x)
    return lambda x: abs(x) * -1

