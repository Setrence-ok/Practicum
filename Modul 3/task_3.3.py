def compress_string(strk):
    if not isinstance(strk, str):
        raise TypeError("it is not a string")
    if strk == "":
        return ""
    else:
        x = ""
        y = ""
        count = 0
        for char in strk:
            if x == "":
                x = char
                count += 1
            elif char == x:
                count += 1
            else:
                y += (x + str(count))
                x = char
                count = 1
        y += (x + str(count))
        return y

# Пример использования
test_str = "dhdhfhdfdhffffhhh"
result = compress_string(test_str)
print("Сжатая строка:", result)