# 2.Для натурального n создать список, состоящий из элементов последовательности 3n + 1

n = int(input("Введите натуральное число n: "))
result = []
for i in range(1, n + 1):
    result.append(3*i + 1)
print(*result, sep=', ')