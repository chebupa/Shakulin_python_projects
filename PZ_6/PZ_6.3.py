
# Напиши решение задачи на python:
# Дан список размера N и целое число К (1 < K < N).
# Осуществить сдвиг элементов списка вправо на К позиций
# (при этом А перейдет в Ак+1, А2 — в Ак+2,..AN-к — в AN, а исходное значение и последних элементов будет потеряно).
# Первые к элементов полученного списка положить равными 0.


def shift_list_right(arr, k):
    n = len(arr)
    for i in range(n - 1, k - 1, -1):
        arr[i] = arr[i - k]
    for i in range(k):
        arr[i] = 0
    return arr


# Пример использования
while True:
    try:
        N = int(input("Введите размер списка A: "))
        A = [int(input(f"Введите элемент A[{i + 1}]: ")) for i in range(N)]
        K = int(input("Введите значение K (1 < K < N): "))

        result = shift_list_right(A, K)

        print("Результат сдвига:", result)
    except ValueError:
        print("Неправильный ввод")

