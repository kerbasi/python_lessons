# Дано число обозначающее день недели. Вывести его название и
# указать является ли он выходным.

try:
    n = int(input("Введите число для вывода дня недели: "))
except:
    print("Вы ввели не целое число!!! Попробуйте снова")
else:
    n -= 1
    week_days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Субота","Воскресенье"]
    if 0 <= n <= 4:
        print(f"Введенное число это {week_days[n]} - не выходной!")
    elif 5 <= n <= 6:
        print(f"Введенное число это {week_days[n]} - выходной!")
    else:
        print(f"Введенное число находится вне диапазона дней недели")