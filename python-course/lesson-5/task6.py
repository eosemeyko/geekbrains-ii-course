import re

result = dict()

with open('task6-lessons', 'r') as f:
    lines = f.readlines()
    for line in lines:
        elements = line.rstrip().split()
        label = elements[0]
        nums = list(map(int, re.findall(r'\d+', line)))
        result[label] = sum(nums)

print(result)
