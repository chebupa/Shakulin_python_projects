
# Сгенерировать словарь вида {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36},
# удалить из него второй и третий элементы. Отобразить исходный и получившийся словарь. Использовать for, range.


def generate_dict(quantity: int):
    dict = { i: i**2 for i in range(0, quantity + 1) }
    return dict


def filter_dict(dictionary, indexes):
    keys_to_remove = [key for i, key in enumerate(dictionary.keys()) if i in indexes]
    for key in keys_to_remove:
        dictionary.pop(key)
    return dictionary


while True:
    try:
        quantity = int(input("Введите номер: "))
        dict = generate_dict(quantity=quantity)
        print(filter_dict(dict, [1, 3]))
        break
    except ValueError:
        print("Неверный ввод")
