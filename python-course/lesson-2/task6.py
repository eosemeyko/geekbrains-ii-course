from typing import List

from utils import get_input_no_empty

products: list = []
product_keys: List[str] = ['название', 'цена', 'количество', 'ед']
end_buttons = ['y', 'да']

# Добавление продуктов в базу
i = 1
while True:
    product: dict = {}
    for key in product_keys:
        product[key] = get_input_no_empty(key)
    products.append((i, product))
    i += 1
    print(f'\nДобавлено продуктов: {len(products)}')

    if input('Завершить добавление?  да/y: ').lower() in end_buttons:
        break
    print('\n')

# Вывод полученного списка продуктов
if input('\nПоказать список продуктов? да/y: ').lower() in end_buttons:
    print(products)

# Формируем аналитику
result = {k: [] for k in product_keys}
for key in product_keys:
    for _, product in products:
        if product[key] not in result.get(key):
            result[key].append(product[key])

# Вывод результата
print('\nАналитика по товарам:')
print(result)
