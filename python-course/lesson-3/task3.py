def my_func(x: int, y: int, z: int) -> int:
    num_list: list = [x, y, z]
    sum_list: list = []
    for _ in range(0, 2):
        value = max(num_list)
        num_list.remove(value)
        sum_list.append(value)
    return sum(sum_list)


print(my_func(10, 57, 78))
