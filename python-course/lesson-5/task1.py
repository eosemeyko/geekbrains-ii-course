file = open('task1-input.txt', 'w+')

i = 1
while True:
    string: str = input(f'Введите текст (строка {i}): ')
    if len(string):
        file.write(string)
        file.write('\n')
        i += 1
    else:
        print(f'Текст сохранен в файл')
        break


print(file.read())
file.close()
