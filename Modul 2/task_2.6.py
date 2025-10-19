def armstr(num):
    if type(num) is not int:
        raise TypeError("Input must be an integer")
    if num < 0:
        raise ValueError("Input must be non-negative")
    if num == 0:
        return

    first = True  # Флаг для правильной печати без начальной запятой

    for number in range(1, num + 1):
        original = number
        digit_count = 0
        temp = number

        # Считаем количество цифр
        while temp > 0:
            temp = temp // 10
            digit_count += 1

        # Считаем сумму цифр в степени digit_count
        sum_pow = 0
        temp = number
        while temp > 0:
            digit = temp % 10
            sum_pow += digit ** digit_count
            temp = temp // 10

        # Проверяем, является ли число числом Армстронга
        if sum_pow == original:
            if first:
                print(number, end="")
                first = False
            else:
                print(", ", end="")
                print(number, end="")

# Пример использования
num = int(input("Введите верхнюю границу диапазона: "))
armstr(num)