
# Средствами языка Python сформировать два текстовых файла (txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Индекс первого минимально элемента первого файла:
# Индекс последнего максимального элемента второго файла:
# Элементы кратные 4 первого и второго файлов:

import random


def generate_file(filename):
    with open(filename, 'w') as f:
        numbers = [random.randint(-100, 100) for _ in range(20)]
        f.write(" ".join(map(str, numbers)))

def read_numbers_from_file(filename) -> [int]:
    with open(filename, 'r') as f:
        return list(map(int, f.read().split()))


def process_files(file1, file2, result_file):
    numbers1 = read_numbers_from_file(file1)
    numbers2 = read_numbers_from_file(file2)

    count1 = len(numbers1)
    count2 = len(numbers2)

    index_min1 = numbers1.index(min(numbers1))
    index_max2 = max((i for i, v in enumerate(numbers2) if v == max(numbers2)))

    multiples_of_4 = [num for num in numbers1 + numbers2 if num % 4 == 0]

    with open(result_file, 'w') as f:
        f.write(f"Элементы первого файла: {numbers1}\n")
        f.write(f"Элементы второго файла: {numbers2}\n")
        f.write(f"Количество элементов первого файла: {count1}\n")
        f.write(f"Количество элементов второго файла: {count2}\n")
        f.write(f"Индекс первого минимального элемента первого файла: {index_min1}\n")
        f.write(f"Индекс последнего максимального элемента второго файла: {index_max2}\n")
        f.write(f"Элементы, кратные 4, из обоих файлов: {multiples_of_4}\n")


# Генерация файлов
# generate_file("file1.txt")
# generate_file("file2.txt")

# Обработка файлов и запись результата
process_files("file1.txt", "file2.txt", "result.txt")
