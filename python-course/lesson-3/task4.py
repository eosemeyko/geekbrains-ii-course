def my_func(x: int, y: int) -> float:
    value = 1
    while y < 0:
        value = value * 1/x
        y = y + 1
    return value


nums = [2, -7]
print(nums[0] ** nums[1])
print(my_func(*nums))
