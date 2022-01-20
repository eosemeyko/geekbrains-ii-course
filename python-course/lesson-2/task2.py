elements: str = input("Введите элементы списка: ")
list_els: list = elements.split()
print(list_els)

for i in range(0, len(list_els) - 1, 2):
    list_els[i], list_els[i+1] = list_els[i+1], list_els[i]
print(list_els)
