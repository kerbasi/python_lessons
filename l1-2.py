# Найти максимальное из пяти чисел.

from random import random

numbers_list = []
for i in range(5):
    numbers_list.append(round(random() * 100))

print((numbers_list))
print(max(numbers_list))