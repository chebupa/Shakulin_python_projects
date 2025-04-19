
# Из предложенного текстового файла (text18-31.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв.
# Сформировать новый файл, в который поместить строку наименьшей длины.


import string


def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-16-le') as file:
            lines = file.readlines()

            # Вывод содержимого файла
            print("Содержимое файла:")
            for line in lines:
                print(line, end='')


            # Подсчет буквенных символов
            letter_count = sum(letter.isalpha() for line in lines for letter in line)
            print(f"\nКоличество буквенных символов: {letter_count}")

            # Нахождение строки минимальной длины
            if lines:
                min_length_line = min(lines, key=len).strip()

                # Запись строки минимальной длины в новый файл
                with open(output_filename, 'w', encoding='utf-8') as out_file:
                    out_file.write(min_length_line)
                print(f"Строка минимальной длины записана в {output_filename}")
            else:
                print("Файл пуст.")
    except FileNotFoundError:
        print(f"Файл {input_filename} не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")


# Запуск скрипта
process_file('text18-31.txt', 'shortest_line.txt')
