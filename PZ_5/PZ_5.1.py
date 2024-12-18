
# Составить функцию, которая выполнит суммирования числового ряда.

# Решение

def sum_row(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

# Пример использования
while True:
    try:
        num1 = int(input("Введите число 1: "))
        num2 = int(input("Введите число 2: "))
        print(f"Сумма чисел от {num1} до {num2}: {sum_row(num1, num2)}")
    except ValueError:
        print("Неверный ввод")
