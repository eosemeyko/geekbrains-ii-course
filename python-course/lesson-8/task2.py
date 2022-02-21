from functools import reduce


def is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


class OwnError(Exception):
    pass


class NotIntegerError(Exception):
    pass


class ZeroDivError(Exception):
    pass


while True:
    try:
        user_input = input('Введите числа по порядку: ')
        value_lst = user_input.split()

        # Проверка на числовые значения
        if not all(is_number(n) for n in value_lst):
            raise NotIntegerError(f'Вы ввели не числа')

        # Изменение всех значений на числовой тип
        value_lst = list(map(int, value_lst))

        # Проверка наличия отрицательных чисел
        if any(n < 0 for n in value_lst):
            raise OwnError('Отрицательные числа недопустимы')

        # Проверка наличия нулей
        if any(n == 0 for n in value_lst):
            raise ZeroDivError('Деление на ноль невозможно')

        print(reduce(lambda x, y: x // y, value_lst))
    except (OwnError, NotIntegerError, ZeroDivError) as err:
        print(err)
    else:
        break

