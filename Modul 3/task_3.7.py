def is_palindrome(strk):
    if not isinstance(strk, str):
        raise TypeError('strk must be a string')

    new_strk = []
    if strk != "":
        for char in strk:
            new_strk.append(char)
        new_strk.reverse()
        res = ''.join(new_strk)
        if res == strk:
            return True
        else:
            return False
    return True


# Пример использования
print(is_palindrome("12321"))