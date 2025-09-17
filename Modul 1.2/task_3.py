import math

def factorial(number):
    if n == 0:
        return 1
    else:
        num = math.factorial(number)
        return num

n = int(input("Введите число:"))

if n < 0:
    print("Факториал отрицательного числа не существует")
else:
    print("Факториал равен: ", factorial(n))
