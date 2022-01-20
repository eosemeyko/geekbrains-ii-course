def get_input_num(msg: str) -> int:
    """Запрос ввода с клавиатуры и проверка числа"""

    while True:
        value = input(f'\nВведите {msg}: ')
        if not value.isnumeric():
            print(f'Вы ввели не {msg}. Попробуйте снова: ')
        else:
            break
    return int(value)


def get_input_no_empty(msg: str):
    """Проверка на пустой ввод"""

    while True:
        value: str = input(f'Введите {msg}: ')
        if len(value):
            break
        else:
            print(f'Строка пустая! Попробуйте снова')
    return int(value) if value.isnumeric() else value


def get_month_num() -> int:
    """Запрос номера месяца"""
    num_month = range(1, 13)

    while True:
        value = get_input_num("номер месяца")
        if value not in num_month:
            print(f'Введите число от 1 - 12')
        else:
            break
    return value
