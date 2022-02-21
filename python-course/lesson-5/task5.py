FILENAME = 'task5-text'

# SAVE TO FILE
with open(FILENAME, 'w+') as f:
    f.write(" ".join(list([str(n) for n in range(1, 40, 2)])))

# READ FROM FILE
file = open(FILENAME, 'r')

text = file.read()
numbers = list(map(int, text.split()))
print(sum(numbers))

file.close()
