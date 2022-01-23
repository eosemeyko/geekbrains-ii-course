from utils import get_input_num


def division_func(x: int, y: int) -> float:
    return x / y


value1: int = get_input_num('первое число')
value2: int = get_input_num('второе число')

print(f'Результат: {value1} / {value2} = {division_func(value1, value2)}')
