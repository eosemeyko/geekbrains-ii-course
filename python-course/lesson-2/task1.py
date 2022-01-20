import os
from utils import get_input_num


class TestingClass:
    pass


TYPE_ITEMS = [
    'the best course',
    777, 1.5, complex(3), True, None,
    [3, 2, 1], {'one': 1}, {1, 2}, (6, 7),
    get_input_num, abs, os.path, TestingClass(), bytes()
]
for i in TYPE_ITEMS:
    print(type(i))
