from utils import get_input_num

# Stage 1
a, b = 7, 6
print(f'a = {a}', 'and', f'b = {b}')
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b}')
# print(f'{a} ** {b} = {a ** b}')
for op in ['+', '-', '*', '/', '**']:
    print(f"{a} {op} {b} = {eval(f'{a} {op} {b}')}")

print(get_input_num("число"))

input_str: str = input("\nВведите какой-нибудь текст: ")
print(input_str)

# Stage 2
import time  # noqa
input_sec = get_input_num("время в секундах")
parse_time = time.gmtime(int(input_sec))
print(f'hours: {parse_time.tm_hour} minutes: {parse_time.tm_min} seconds: {parse_time.tm_sec}')
print(time.strftime('%H:%M:%S', parse_time))

# Stage 3
input_num = get_input_num('число')
n_str: str = str(input_num)
n_two: int = int(n_str + n_str)
n_three: int = int(n_str + n_str + n_str)
print(f'sum {input_num} + {n_two} + {n_three} = {input_num + n_two + n_three}')


# Stage 4
def max_int(value):
    i = 0
    while value != 0:
        i = max(i, value % 10)
        value //= 10
    return i


input_num: int = get_input_num('число')
print(max_int(input_num))

# Stage 5


# Stage 6
