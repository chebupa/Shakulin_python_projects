# Сгенерировать двумерный список, в которой элементы больше 10 заменяются на 0.


import random


def generate_matrix(rows: int, cols: int) -> [[int]]:
    return [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

def process_matrix(matrix: [[int]]) -> [[int]]:
    return [[0 if val > 10 else val for val in row] for row in matrix]

matrix = generate_matrix(5, 5)
processed_matrix = process_matrix(matrix)


print("Оригинальная матрица:")
for row in matrix:
    print(row)

print("\nПосле замены элементов > 10 на 0:")
for row in processed_matrix:
    print(row)