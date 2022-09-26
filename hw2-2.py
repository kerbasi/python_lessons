# Написать программу получающую набор произведений чисел от 1 до N.

n = int(input("Введите число n: "))
num = 1
result = [num]
for i in range(2, n + 1):
    num *= i
    result.append(num)
print(*result)