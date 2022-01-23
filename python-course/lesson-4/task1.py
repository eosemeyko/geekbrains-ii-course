from sys import argv

if len(argv) < 4:
    print("Необходимо ввести 3 параметра при запуске скрипта")
    print("Выработка в часах, ставка в час, премия")
    print('Например:')
    print(f"python {argv[0]} 180 1800 50000")
    exit()


try:
    production: int = int(argv[1])
    bid: int = int(argv[2])
    premium: int = int(argv[3])
    print(production * bid + premium)
except ValueError:
    print("Параметры должны содержать только цифры")
    exit()
