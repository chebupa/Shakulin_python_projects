# Составить генератор (yield), который преобразует все буквенные символы в заглавные.


def uppercase_generator(text):
    for char in text:
        if char.isalpha():
            yield char.upper()
        else:
            yield char


text = "Hello, World! 123"
for char in uppercase_generator(text):
    print(char, end="")