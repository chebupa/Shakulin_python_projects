
# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия

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

bank = Bank(99999, 45)
print(bank.calculate_percent_accrual())
print(bank.calculate_percent_removal())
