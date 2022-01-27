from utils import get_month_num

input_month: int = get_month_num()
months_types: dict = {
    'зима': [1, 2, 12], 'весна': [3, 4, 5],
    'лето': [6, 7, 8], 'осень': [9, 10, 11],
}

for name, month_list in months_types.items():
    if input_month in month_list:
        print(f'Время года: {name}')
        break
