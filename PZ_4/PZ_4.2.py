
# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления определить, имеется ли в записи числа N цифра «2».
# Если имеется, то вывести TRUE, если нет - вывести FALSE.

def has_digit_two(n):
    while n > 0:
        if n % 10 == 2:
            return True
        n //= 10 # удаляет последнюю цифру числа
    return False

# Пример использования
while True:
    try:
        N = int(input("Введите число N (>0): "))
        if N > 0:
            print(has_digit_two(N))
            break
        else:
            print("Ошибка: число должно быть больше 0")
    except ValueError:
        print("Неправильный ввод")

