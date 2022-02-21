with open('task2-text', 'r') as file:
    lines = file.readlines()
    print(f'Количество строк: {len(lines)}\n')

    for k, l in enumerate(lines, 1):
        print(f'В {k} строке слов {len(l.split())}')
