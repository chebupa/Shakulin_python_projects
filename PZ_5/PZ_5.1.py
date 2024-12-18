
# Составить функцию, которая выполнит суммирования числового ряда.

# Решение
def sum_row(n: int):
    return sum(range(1, n + 1))

# Пример использования
while True:
    try:
        N = int(input("Введите число N: "))
        print(f"Сумма чисел от 1 до {N}: {sum_row(N)}")
    except ValueError:
        print("Неверный ввод")
