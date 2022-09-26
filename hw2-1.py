# Подсчитать сумму цифр в вещественном числе.

n = float(input("Введите вещественное число n: "))
sum = 0
for digit in str(n).replace(".", ""):
    sum += int(digit)
print(sum)