
import sqlite3
from itertools import product


class Main:

    def __init__(self, conn):
        self.conn = conn

    def run(cls, conn):
        instance = cls(conn)
        instance.create_table()
        instance.menu()

    def create_table(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products(
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name VARCHAR(99) NOT NULL,
                product_quantity INT NOT NULL,
                product_price_opt FLOAT NOT NULL
            )
        ''')
        self.conn.commit()

    def menu(self):
        while True:
            print("=== Меню управления товарами ===")
            print("1. Добавить товар")
            print("2. Показать все товары")
            print("3. Удалить товар")
            print("4. Обновить товар")
            print("5. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.show_all_products()
            elif choice == '3':
                self.delete_product()
            elif choice == '4':
                self.update_product()
            elif choice == '5':
                print("Выход из программы.")
                break
            else:
                print("Неверный ввод. Попробуйте снова.\n")

    def show_all_products(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Products')
        points = cursor.fetchall()
        if not points:
            print("Нет товаров в базе данных.\n")
        else:
            for point in points:
                print(point)
            print()

    def add_product(self):
        while True:
            try:
                name = str(input("Введите название: "))
                break
            except ValueError:
                print("Ошибка ввода. Введите целое число.")
        while True:
            try:
                quantity = int(input("Введите количество: "))
                break
            except ValueError:
                print("Ошибка ввода. Введите число.")
        while True:
            try:
                price = float(input("Введите оптовую стоимость: "))
                break
            except ValueError:
                print("Ошибка ввода. Введите число.")

        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO Products (product_name, product_quantity, product_price_opt)
            VALUES (?, ?, ?)
        ''', (name, quantity, price))
        self.conn.commit()
        print("Товар успешно добавлен!\n")

    def delete_product(self):
        while True:
            try:
                product_id = int(input("Введите ID товара для удаления: "))
                break
            except ValueError:
                print("Ошибка ввода ID. Введите целое число.")
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Products WHERE product_id = ?', (product_id,))
        point = cursor.fetchone()
        if point is None:
            print("Товар с таким ID не найден.\n")
            return
        cursor.execute('DELETE FROM Products WHERE product_id = ?', (product_id,))
        self.conn.commit()
        print("Товар успешно удален.\n")

    def update_product(self) -> None:
        while True:
            try:
                product_id = int(input("Введите ID товара для обновления: "))
                break
            except ValueError:
                print("Ошибка ввода ID. Введите целое число.")

        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Products WHERE product_id = ?', (product_id,))
        product = cursor.fetchone()
        if product is None:
            print("Товар с таким ID не найден.\n")
            return

        print(f"Текущие данные: Название: {product[1]}, Кол-во: {product[2]}, Оптовая цена: {product[3]}")

        name = input("Новое название: ")
        quantity_input = input("Новое количество: ")
        price_input = input("Новое оптовую цену: ")

        new_name = name if name else product[1]
        new_quantity = int(quantity_input) if quantity_input else product[2]
        new_price = float(price_input) if price_input else product[3]

        cursor.execute('''
            UPDATE Products
            SET product_name = ?, product_quantity = ?, product_price_opt = ?
            WHERE product_id = ?
        ''', (new_name, new_quantity, new_price, product_id))
        self.conn.commit()
        print("Товар успешно обновлен.\n")

if __name__ == "__main__":
    db_name = 'products.db'
    connection = sqlite3.connect(db_name)
    try:
        Main.run(Main, connection)
    finally:
        connection.close()
