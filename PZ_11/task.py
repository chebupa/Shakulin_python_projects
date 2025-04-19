
def create_new_file():
    with open("new_file.txt", "w") as file:
        file.write("Это новый текстовый файл")
        file.close()

try:
    # Способ 1
    # with open("new_file.txt", "r") as file:
    #     file_content = file.read()
    #
    #     with open("new_file.txt", "w") as file:
    #         file.write(file_content)
    #         file.close()
    #
    #     file.close()

    # Способ 2
    with open("new_file.txt", "r") as file:
        file.close()
    with open("new_file.txt", "w") as file:
        file.write("Текстовый файл уже существовал, вот новое содержимое")
        file.close()
except FileNotFoundError:
    create_new_file()
