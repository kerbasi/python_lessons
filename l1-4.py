#показать первую цифру дробной части числа
import math
n = float(input())

print(math.floor(n * 10 % 10))