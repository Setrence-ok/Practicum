def tribonacci(n):
    if type(n) is not int:
        raise ValueError("Input must be an integer.")
    elif n < 0:
        raise ValueError("Input must be a non-negative integer.")
    else:
        a, b, c = [0, 0, 1]
        count = 0
        if n == 0:
            tribonacci = a
            return tribonacci
        elif n == 1:
            tribonacci = b
            return tribonacci
        elif n == 2:
            tribonacci = c
            return tribonacci
        else:
            while count < n - 1:
                a, b, c = b, c, a + b + c
                tribonacci = c
                count += 1
            return tribonacci

n = int(input("Введите номер числа Трибоначчи: "))
if type(n) is not int:
    raise ValueError("Input must be an integer.")
else:
    result = tribonacci(n)
    print(f"T({n}) = {result}")