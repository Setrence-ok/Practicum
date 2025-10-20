def count_char(lst, char):
    if not isinstance(lst, list):
        raise TypeError('lst is not a list')
    if not all(isinstance(item, str) for item in lst):
        raise TypeError('char is not a string')
    new_lst = []
    for item in lst:
        if item == "":
            new_lst.append(0)
        else:
            new_lst.append(item.count(char))
    return new_lst

# Пример использования
test_list = ["helloo", "world", ""]
char_to_count = "o"

result = count_char(test_list, char_to_count)
print("Результат:", result)