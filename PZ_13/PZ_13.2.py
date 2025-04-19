# В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2 раза.


import random


def generate_matrix(rows: int, cols: int) -> [[int]]:
    return [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]

def process_matrix(matrix: [[int]]) -> [[int]]:
    return [
        [
            val if i == j else val * 2
            for j, val in enumerate(row)
        ]
        for i, row in enumerate(matrix)
    ]

matrix = generate_matrix(5, 5)
processed_matrix =  process_matrix(matrix)


print("Оригинальная матрица:")
for row in matrix:
    print(row)

print("\nПосле обработки:")
for row in processed_matrix:
    print(row)