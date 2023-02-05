import library


def deposit_amount(default=None):
    if default:
        suma = default
    else:
        suma = library.get_user_number('What is your deposit amount? ')
    hryvnas, cents = str(suma).split('.')
    result_uah = hryvnas + library.get_hryvnas(hryvnas)
    coins = cents + library.get_coins(int(cents))
    print(result_uah, coins)



