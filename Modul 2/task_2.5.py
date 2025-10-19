def bin_kef(num, kef):
    if type(num) is not int or type(kef) is not int:
        raise TypeError("Arguments must be integers.")
    if num < 0 or kef < 0 or kef > num:
        raise ValueError("Invalid values: require 0 ≤ kef ≤ num")
    if kef > num - kef:
        kef = num - kef
    result = 1
    for i in range(1, kef + 1):
        result = result * (num - kef + i) // i
    return result
num = int(input("Введите число n: "))
kef = int(input("Введите число k: "))
result = bin_kef(num, kef)
print(f"C({num}, {kef}) = {result}")