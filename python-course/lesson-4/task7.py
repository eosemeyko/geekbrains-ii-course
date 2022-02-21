import math

number: int = 7


def fact(n: int) -> next:
    v: int = 1
    for i in range(1, n + 1):
        v = v * i
        yield v


print(f'Math {math.factorial(number)}')
print([a for a in fact(number)])
