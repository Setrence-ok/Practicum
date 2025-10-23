from os import remove


def is_palindrome(string):
    if not isinstance(string, str):
        raise TypeError('strk must be a string')

    new_strk = []
    if string != "":
        for char in string:
            new_strk.append(char)
        new_strk.reverse()
        res = ''.join(new_strk)
        if res == string:
            return True
        else:
            return False
    return True

def is_palindrome_recursive(string):
    # Приводим строку к нижнему регистру и удаляем пробелы
    string = string.replace(" ", "").lower()

    # Базовый случай: если строка пустая или состоит из одного символа
    if len(string) <= 1:
        return True

    # Проверяем крайние символы
    if string[0] != string[-1]:
        return False

    # Рекурсивный вызов для оставшейся строки
    return is_palindrome_recursive(string[1:-1])


# Получение ввода от пользователя
string_input = "12321"

# Вывод результатов
print("Обычный метод:", is_palindrome(string_input))
print("Рекурсивный метод:", is_palindrome_recursive(string_input))