
# Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Найти длину самого короткого слова.


def shortest_word_length(s):
    words = s.strip().split() # Удаляем лишние пробелы и разбиваем строку на слова
    if not words: return 0

    min_length = min(len(word) for word in words)

    return min_length


input_string = "   Это  пример строки с   несколькими   пробелами   "
result = shortest_word_length(input_string)
print("Длина самого короткого слова:", result)

