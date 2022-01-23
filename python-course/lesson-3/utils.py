from typing import Union


def get_input_num(msg: str) -> int:
    """Запрос ввода с клавиатуры и проверка числа"""

    while True:
        value = input(f'\nВведите {msg}: ')
        if not value.isnumeric():
            print(f'Вы ввели не {msg}. Попробуйте снова')
        elif int(value) < 1:
            print('Введите значение больше 0')
        else:
            break
    return int(value)


def get_input_no_empty(msg: str) -> Union[str, int]:
    """Проверка на пустой ввод"""

    while True:
        value: str = input(f'Введите {msg}: ')
        if not len(value):
            print(f'Строка пустая! Попробуйте снова')
        else:
            break
    return int(value) if value.isnumeric() else value


def check_is_digit(value: str) -> bool:
    if value.isdigit():
        return True
    else:
        try:
            float(value)
            return True
        except ValueError:
            return False
