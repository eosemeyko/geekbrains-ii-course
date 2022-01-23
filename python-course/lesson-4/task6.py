from itertools import count, cycle

# Целые числа
results1: list = []
for v in count(3):
    if v >= 10:
        break
    results1.append(v)
print(results1)

# Повторяющиеся элементы списка
numbers = [1, 2, 3, 4, 5, 6, 7]
results2: list = []
i: int = 0
rep: bool = False

for v in cycle(numbers):
    results2.append(v)
    i += 1
    if i >= len(numbers):
        if not rep:
            rep = True
            i = 0
        else:
            break
print(results2)
