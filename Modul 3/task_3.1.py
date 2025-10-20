def replace_characters(lst, old, new):
    if len(lst) == 0:
        return lst
    else:
        new_lst = []
        for char in lst:
            new_char = char.replace(old, new)
            new_lst.append(new_char)
        return new_lst

# Пример использования
test_list = ["hello", "world"]
old_char = "l"
new_char = "m"

result = replace_characters(test_list, old_char, new_char)
print("Результат:", result)