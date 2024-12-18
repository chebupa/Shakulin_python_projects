
# Дан список А размера N.
# Сформировать новый список В того же размера по следующему правилу:
# элемент Вк равен сумме элементов списка А с номерами от 1 до К.

def create_new_list(a):
    b = []
    total_sum = 0
    for i in range(len(a)):
        total_sum += a[i]  # Добавляем элемент A[i] к сумме
        b.append(total_sum)  # Добавляем текущую сумму в список B
    return b


while True:
    try:
        N = int(input("Введите размер списка A: "))
        A = [int(input(f"Введите элемент A[{i + 1}]: ")) for i in range(N)]

        B = create_new_list(A)

        print("Новый список B:", B)
    except ValueError:
        print("Неправильный ввод")

