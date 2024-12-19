
# Дан целочисленный список размера N.
# Увеличить все четные числа, содержащиеся в списке, на исходное значение первого четного числа.
# Если четные числа в списке отсутствуют, то оставить список без изменений.

def increase_even_numbers(lst):
    # Ищем первое четное число в списке
    for num in lst:
        if num % 2 == 0:
            even_number = num
            # Увеличиваем все четные числа на найденное
            for i in range(len(lst)):
                if lst[i] % 2 == 0:
                    lst[i] += even_number
            break
    return lst

# Пример использования
while True:
    try:
        N = int(input("Введите размер списка N: "))
        lst = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]

        result = increase_even_numbers(lst)

        print("Результат:", result)
        break
    except ValueError:
        print("Неправильный ввод")

