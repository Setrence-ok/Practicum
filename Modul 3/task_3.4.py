def sets_intersection(*sets):
    print(sets)
    if not (isinstance(s, set) for s in sets):
        raise TypeError('sets must be a set')

    if 0 > len(sets) > 100:
        raise ValueError('sets must contain at most 100 elements')

    if len(sets) == 0:
        return sets
    elif len(sets) == 1:
        return sets
    else:
        a = sets[0]
        for set in sets:
            if  a == len(sets) - 1:
                return sets()
            else:
                a = a.intersection(set)
        return a
# Пример использования
print(sets_intersection({2, 5, 6}))