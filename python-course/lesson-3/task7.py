from task6 import upper_func


def my_func(value: str) -> str:
    return ' '.join(upper_func(word[0]) + word[1:] for word in value.split())


print(my_func('hello world'))
