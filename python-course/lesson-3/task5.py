from utils import check_is_digit


results: int = 0

while True:
    values: str = input('Введите строку чисел (через пробел): ')
    elements: list = values.split()
    elements_nums: list = list(filter(lambda x: check_is_digit(x), elements))
    results += sum(list(map(int, elements_nums)))
    print(results)

    # Фильтруем по символам, если находим завершаем цикл
    if elements_no_nums := list(filter(lambda x: not check_is_digit(x), elements)):
        print(f'Вы ввели не числовое значение {", ".join(elements_no_nums)}. Останов')
        break
