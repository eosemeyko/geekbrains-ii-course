def is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


class NotIntegerError(Exception):
    pass


num_list = list()

while True:
    try:
        user_input = input('Введите числа по порядку (или stop для остановки): ')
        if user_input == 'stop':
            break

        value_lst = user_input.split()

        # Проверка на числовые значения
        if not all(is_number(n) for n in value_lst):
            raise NotIntegerError(f'Вы ввели не числа')

        # Сохранение значений в список с конвертацией в числа
        num_list += list(map(int, value_lst))
        print(num_list)

    except NotIntegerError as err:
        print(err)

print(num_list)
