# Вывести на экран числа от -N до N.
try:
    n = int(input("Введите число: "))
except:
    print("Вы ввели не целое число!!! Попробуйте снова")
else:
    for i in range(-n, n + 1):
        print(i, end = " ")
