from typing import Optional

# Даны четыре целых числа, одно из которых отлично от трех других, равных между собой.
# Определить порядковый номер числа, отличного от остальных.

while True:
    try:
        numbers = []
        for i in range(4):
            num = int(input(f"Введите число {i + 1}: "))
            numbers.append(num)

        unique_index: Optional[int] = None
        for i in range(len(numbers)):
            if numbers.count(numbers[i]) == 1:
                unique_index = i + 1  # Порядковый номер (начиная с 1)

        if (index := unique_index) is not None:
            print(f"Порядковый номер числа, отличного от остальных: {index}")
        else:
            print("Все числа одинаковы.")

        break
    except ValueError:
        print("Неверный ввод")
