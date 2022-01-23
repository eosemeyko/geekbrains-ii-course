def int_func(value: str) -> str:
    return ' '.join(word[0].upper() + word[1:] for word in value.split())


print(int_func('hello world'))