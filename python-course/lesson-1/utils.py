def get_input_num(msg: str) -> int:
    """Запрос ввода с клавиатуры и проверка числа"""

    while True:
        value = input(f'\nВведите {msg}: ')
        if not value.isnumeric():
            print(f'Вы ввели не {msg}. Попробуйте снова: ')
        else:
            break
    return int(value)
