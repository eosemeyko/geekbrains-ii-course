numbers: list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([n for n in numbers if len(list(filter(lambda x: x == n, numbers))) < 2])
