# Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для некоторой организации.
# БД должна содержать таблицу Торговая точка со следующей структурой записи:
# этаж, площадь, наличие кондиционера и стоимость аренды в день.


import sqlite3


class Main:

    def __init__(self, conn):
        self.conn = conn

    def run(cls, conn):
        instance = cls(conn)
        instance.create_table()
        instance.menu()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TradePoint (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                floor INTEGER NOT NULL,
                area REAL NOT NULL,
                air_conditioner BOOLEAN NOT NULL,
                daily_rent REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add_trade_point(self):
        floor = int(input("Введите этаж: "))
        area = float(input("Введите площадь (в кв.м): "))
        air_conditioner = input("Есть кондиционер? (да/нет): ").strip().lower() == 'да'
        daily_rent = float(input("Введите стоимость аренды в день: "))

        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO TradePoint (floor, area, air_conditioner, daily_rent)
            VALUES (?, ?, ?, ?)
        ''', (floor, area, air_conditioner, daily_rent))
        self.conn.commit()
        print("Точка успешно добавлена!\n")


    def show_all_trade_points(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM TradePoint')
        points = cursor.fetchall()
        if not points:
            print("Нет торговых точек в базе данных.\n")
        else:
            for point in points:
                print(f"ID: {point[0]} | Этаж: {point[1]} | Площадь: {point[2]} кв.м | "
                      f"Кондиционер: {'Есть' if point[3] else 'Нет'} | "
                      f"Аренда в день: {point[4]} руб.")
            print()

    def delete_trade_point(self):
        trade_point_id = int(input("Введите ID торговой точки для удаления: "))
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM TradePoint WHERE id = ?', (trade_point_id,))
        point = cursor.fetchone()
        if point is None:
            print("Торговая точка с таким ID не найдена.\n")
            return
        cursor.execute('DELETE FROM TradePoint WHERE id = ?', (trade_point_id,))
        self.conn.commit()
        print("Торговая точка успешно удалена.\n")

    def handle_user_errors(self, func):
        try:
            func()
        except ValueError:
            print("Ошибка ввода. Попробуйте снова.\n")
        except Exception as e:
            print(f"Произошла ошибка: {e}\n")

    def menu(self):
        while True:
            print("=== Меню управления торговыми точками ===")
            print("1. Добавить торговую точку")
            print("2. Показать все торговые точки")
            print("3. Удалить торговую точку")
            print("4. Выход")
            choice = input("Выберите действие: ").strip()

            if choice == '1':
                self.handle_user_errors(self.add_trade_point)
            elif choice == '2':
                self.handle_user_errors(self.show_all_trade_points)
            elif choice == '3':
                self.handle_user_errors(self.delete_trade_point)
            elif choice == '4':
                print("Выход из программы.")
                break
            else:
                print("Неверный ввод. Попробуйте снова.\n")


if __name__ == "__main__":
    db_name = 'rental.db'
    connection = sqlite3.connect(db_name)
    try:
        Main.run(Main, connection)
    finally:
        connection.close()
