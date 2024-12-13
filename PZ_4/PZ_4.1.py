
# Дано целое число N (>0). Найти значение выражения 1.1 - 1.2 + 1.3 - ... (N слагаемых, знаки чередуются).
# Условный оператор не использовать.

while True:
    try:
        n = int(input("Введите целое число N (>0): "))
        result: int

        for i in range(1, n + 1):
            result = sum(-1 ** (i + 1)) * i

        print(f"Результат: {result}")
    except ValueError:
        print("Неверный ввод")
