from functools import reduce

print(reduce(lambda x, y: x * y, [a for a in range(100, 1001) if a % 2 == 0]))
