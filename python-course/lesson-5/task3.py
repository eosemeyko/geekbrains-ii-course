total = 0

with open('task3-person', 'r') as f:
    persons = f.readlines()
    for p in persons:
        first_name, pay = p.split()
        pay = int(pay)
        total = total + pay

        if pay < 20000:
            print(f'У {first_name} оклад менее 20 тысяч')

    print(f'\nВеличина окладов сотрудников: {total / len(persons)}')
