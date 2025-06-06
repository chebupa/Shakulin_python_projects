from curses.textpad import rectangle


# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота".
# От этого класса унаследуйте классы "Прямоугольник" и "Квадрат".
# Для класса "Квадрат" переопределите методы, связанные с вычислением площади и периметра.


class Figure:

    width: float
    height: float

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return (self.width + self.height) * 2


class Rectangle(Figure):

    def calculate_area(self) -> float:
        return 1

    def calculate_perimeter(self) -> float:
        return 2

class Square(Figure):

    def calculate_area(self) -> float:
        return 3

    def calculate_perimeter(self) -> float:
        return 4


figure = Figure(width=5, height=10)
print(figure.calculate_area())
print(figure.calculate_perimeter())

rectangle = Rectangle(width=5, height=10)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

square = Square(width=5, height=10)
print(square.calculate_area())
print(square.calculate_perimeter())