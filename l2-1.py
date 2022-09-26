# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.

n = int(input("Введите натуральное число n "))
result = ''
result_num = 1
for i in range(n):
    if i == 0:
        result += str(result_num)
        result_num = 1
        result += ', '
    result_num *= -3
    result += str(result_num)
    result += ', '
print(result[0:(len(result) - 2)])
