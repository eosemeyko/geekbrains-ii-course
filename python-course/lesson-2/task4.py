value: str = input('Введите слова через пробелы: ')
value_list: list = value.split()

for i, v in enumerate(value_list, 1):
    print(f'{i}. {v[:10]}')
