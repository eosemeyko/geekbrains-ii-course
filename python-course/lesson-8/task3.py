def is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


class NotIntegerError(Exception):
    pass


while True:
    try:
        user_input = input('Введите числа по порядку: ')
        value_lst = user_input.split()

        # Проверка на числовые значения
        if not all(is_number(n) for n in value_lst):
            raise NotIntegerError(f'Вы ввели не числа')

        # Сохранение значений в список с конвертацией в числа
        print(list(map(int, value_lst)))

    except NotIntegerError as err:
        print(err)
    else:
        break
