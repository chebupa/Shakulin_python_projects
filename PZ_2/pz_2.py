
# Дни недели пронумерованы следующим образом: 1 — понедельник,
# 2 - вторник, .., 6 — суббота, 7 — воскресенье. Дано целое число К, лежащее в диапазоне
# 1-365. Определить номер дня недели для К-го дня года, если известно, что в этом году 1 января было вторником.

while True:
    try:
        k = int(input("Введите номер дня года (1-365): "))
        day_number = (k + 1) % 7 # 1 января - вторник, номер 2
        print(f"Номер дня недели: { day_number if day_number != 0 else 7 }") # Если результат 0, это воскресенье
        break
    except ValueError:
        print("Неверный ввод")
