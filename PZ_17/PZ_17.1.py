# Задание 1.
# В соответствии с номером варианта перейти по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1).
# https://studfile.net/html/2706/360/html_uTKkMTCo1E.hFYH/htmlconvd-efYkCR62x1.jpg

import tkinter as tk
from tkinter import ttk


class RegistrationForm(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bg='pink')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.create_header()
        self.create_form_fields()
        self.create_age_section()
        self.create_languages_section()
        self.create_format_section()
        self.create_authors_section()
        self.create_buttons()
        self.create_footer()

    def create_header(self):
        tk.Label(self, text="Регистрационная страница электронной библиотеки", bg='pink', font=('Helvetica', 12, 'bold')).pack(pady=5)
        tk.Label(self, text="Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой", bg='pink').pack()

    def create_form_fields(self):
        form_frame = tk.Frame(self, bg='pink')
        form_frame.pack(pady=5)

        tk.Label(form_frame, text="Введите регистрационное имя", bg='pink').grid(row=0, column=0)
        tk.Entry(form_frame).grid(row=0, column=1)

        tk.Label(form_frame, text="Введите пароль", bg='pink').grid(row=1, column=0)
        tk.Entry(form_frame, show='*').grid(row=1, column=1)

        tk.Label(form_frame, text="Подтвердите пароль", bg='pink').grid(row=2, column=0)
        tk.Entry(form_frame, show='*').grid(row=2, column=1)

    def create_age_section(self):
        tk.Label(self, text="Ваш возраст", bg='pink').pack()
        age_frame = tk.Frame(self, bg='pink')
        age_frame.pack()
        ages = ["До 20", "20-30", "30-50", "старше 50"]
        self.age_var = tk.StringVar()
        for age in ages:
            tk.Radiobutton(age_frame, text=age, variable=self.age_var, value=age, bg='pink').pack(side='left')

    def create_languages_section(self):
        tk.Label(self, text="На каких языках читаете:", bg='pink').pack()
        lang_frame = tk.Frame(self, bg='pink')
        lang_frame.pack()
        languages = ["русский", "английский", "французский", "немецкий"]
        self.lang_vars = {}
        for lang in languages:
            var = tk.BooleanVar()
            tk.Checkbutton(lang_frame, text=lang, variable=var, bg='pink').pack(side='left')
            self.lang_vars[lang] = var

    def create_format_section(self):
        tk.Label(self, text="Какой формат данных является для вас предпочтительным?", bg='pink').pack()
        self.format_combo = ttk.Combobox(self, values=["HTML", "Plain text"])
        self.format_combo.current
        self.format_combo.pack()

    def create_authors_section(self):
        tk.Label(self, text="Ваши любимые авторы:", bg='pink').pack()
        self.authors = tk.Text(self, height=3, width=40)
        self.authors.pack()

    def create_buttons(self):
        btn_frame = tk.Frame(self, bg='pink')
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="OK").pack(side='left', padx=5)
        tk.Button(btn_frame, text="Отменить").pack(side='left')

    def create_footer(self):
        tk.Label(self, text="Проверка PHP Лабораторные по базам данных", bg='pink').pack()
        entry = tk.Entry(self, width=50, justify='center')
        entry.insert(0, "Лабораторные по базам данных")
        entry.pack()

        tk.Label(self, text="Сегодня замечательный день.", bg='pink').pack()
        tk.Label(self, text="Я сделал свою первую интернет страничку.", bg='pink').pack()
        tk.Label(self, text="я буду богатым и свободным человеком!", fg='blue', font=('Arial', 10, 'underline'), bg='pink').pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Регистрационная страница электронной библиотеки")
    RegistrationForm(root)
    root.mainloop()