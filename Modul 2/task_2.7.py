def triangle_type(trian1, trian2, trian3):
    if trian1 <= 0 or trian2 <= 0 or trian3 <= 0:
        return "Невозможно"

    if not (trian1 + trian2 > trian3 and
            trian1 + trian3 > trian2 and
            trian2 + trian3 > trian1):
        return "Невозможно"

    if trian1 == trian2 == trian3:
        return "Равносторонний"
    elif trian1 == trian2 or trian1 == trian3 or trian2 == trian3:
        return "Равнобедренный"
    return "Разносторонний"

# Пример использования
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

result = triangle_type(a, b, c)
print(f"Тип треугольника: {result}")