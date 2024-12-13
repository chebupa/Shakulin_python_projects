
# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления определить, имеется ли в записи числа N цифра «2».
# Если имеется, то вывести TRUE, если нет - вывести FALSE.

while True:
    try:
        n = int(input("Введите целое число N (>0): "))
        result: bool

        while n > 0:
            if n % 10 == 2:
                result = True
            n //= 10
        result = False

        print("Имеется ли цифра '2' в числе N:", result)
    except ValueError:
        print("Неверный ввод")
