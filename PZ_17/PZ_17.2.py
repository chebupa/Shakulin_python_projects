# Задание 2.
# Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ NºNº 2 - 9.

# Задача из ПЗ 7.1:
# Даны строки S и S0. Найти количество вхождений строки S0 в строку S.

import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bg='pink')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.pack(pady="5")

        tk.Label(frame, text="Введите строку 1: ").grid(row=0, column=0, sticky="e")
        self.entryOne = tk.Entry(frame)
        self.entryOne.grid(row=0, column=1)

        tk.Label(frame, text="Введите строку 2: ").grid(row=1, column=0, sticky="e")
        self.entryTwo = tk.Entry(frame)
        self.entryTwo.grid(row=1, column=1)

        self.result_label = tk.Label(frame, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=5)

        button = tk.Button(frame, text="Посчитать", command=self.calculate)
        button.grid(row=3, column=0, columnspan=2)

    def calculate(self):
        s = self.entryOne.get()
        s0 = self.entryTwo.get()
        count = s.count(s0)
        self.result_label.config(text=f"Количество вхождений: {count}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PZ_17.2")
    MainWindow(root)
    root.mainloop()