list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
a = max(list_numbers)
i = list_numbers.index(a)
list_numbers.insert(i, list_numbers.pop(-1))
list_numbers.append(list_numbers.pop(i+1))
print(list_numbers)
