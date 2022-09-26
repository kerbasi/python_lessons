# Задать список из n чисел последовательности (1 + 1/n) ** n и вывести на экран их сумму n.

from functools import reduce


n = int(input("Введите число n: "))
list = []
sum = 0
for n in range(1, n + 1):
    num = (1 + 1 / n) ** n
    list.append(num)
    sum += num
print(f"Список из {n} чисел последовательности: ")
print(*list)
print(f"Cумма всех чисел последовательности {sum}")
