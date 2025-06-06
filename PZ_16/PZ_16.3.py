
# Для задачи из блока 1 создать две функции, save_def и load _def,
# которые позволяют сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате.


import pickle


class Bank:
    money_sum: float = 0.0
    percent: float = 0.0

    def __init__(self, money_sum: float, percent: float):
        self.money_sum = money_sum
        self.percent = percent

    def calculate_percent_accrual(self) -> float:
        self.money_sum += self.money_sum * self.percent / 100
        return self.money_sum

    def calculate_percent_removal(self) -> float:
        self.money_sum -= self.money_sum * self.percent / 100
        return self.money_sum

def save_def(bank_objects: list[Bank], filename: str) -> None:
    with open(filename, 'wb') as file:
        pickle.dump(bank_objects, file)

def load_def(filename: str) -> list[Bank]:
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Пример использования
if __name__ == "__main__":
    b1 = Bank(1000, 5)
    b2 = Bank(2000, 3)
    b3 = Bank(1500, 4)

    save_def([b1, b2, b3], 'banks.txt')

    loaded_banks = load_def('banks.dat')
    for bank in loaded_banks:
        print(f"Сумма: {bank.money_sum}, Процент: {bank.percent}")