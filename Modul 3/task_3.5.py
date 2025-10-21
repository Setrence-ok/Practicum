def filter_dict_by_value(d, threshold):
    if type(d) is not dict:
        raise TypeError("d must be a dictionary")
    if threshold is str:
        raise TypeError("threshold must be int or float")

    if len(d) == 0:
        return d
    else:
        new_d = {}
        for k, v in d.items():
            if v > threshold:
                new_d[k] = v
            else:
                continue
        return new_d

# Пример использования
data = {'a': 1, 'b': 2, 'c': 3}
limit = 2
result = filter_dict_by_value(data, limit)
print("Результат:", result)