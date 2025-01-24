
# Даны строки S и S0. Найти количество вхождений строки S0 в строку S.

def count_occurrences(S, S0):
    return S.count(S0)


while True:
    try:
        S = str(input("Введите строку S: "))
        S0 = str(input("\nВведите строку S0: "))
        result = count_occurrences(S, S0)
        print(f"Количество вхождений '{S0}' в строку '{S}': {result}")
        break
    except ValueError:
        print("Неверный ввод")
