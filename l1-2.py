import math
from random import Random, random
from xml.etree.ElementInclude import include


import math
#Найти максимальное из 5 чисел
numbers_list = [3,5,6,3,7]
for i in range(5):
    numbers_list[i] = round(random() * 10)


print((numbers_list))
print(max(numbers_list))