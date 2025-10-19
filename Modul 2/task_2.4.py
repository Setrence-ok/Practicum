def decimal_to_binary(num):
    if type(num) is not int:  # Строгая проверка типа (исключает bool)
        raise TypeError("Input must be an integer.")
    if num < 0:
        raise ValueError("Only non-negative integers are allowed.")

    if num == 0:
        return "0"

    binary_str = ""
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num = num // 2
    return binary_str

num = int(input("Введите десятичное число: "))
binary = decimal_to_binary(num)
print(f"Двоичное представление: {binary}")