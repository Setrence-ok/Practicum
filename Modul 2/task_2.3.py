def how_many_times(message):
    if type(message) == str:
        if all(char in " abcdefghijklmnopqrstuvwxyz" for char in message):
            clicks = 0
            for char in message:
                if char == ' ':
                    continue
                else:
                    char_ord = ord(char) - ord('a') + 1
                    clicks += char_ord
            return clicks
        else:
            raise ValueError("String must contain only lowercase a-z letters or spaces")
    else:
        raise TypeError("Input must be a string")
# Пример использования
message = input("Введите сообщение (строчные буквы): ")
clicks = how_many_times(message)
print(f"Количество нажатий: {clicks}")