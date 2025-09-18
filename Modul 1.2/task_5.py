

def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

def solve_quadratic(a, b, c):
    D = discriminant(a, b, c)
    if D < 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        f = "x1 = ", x1, "x2 = ", x2
        return f
    elif D == 0:
        x = -b / (2 * a)
        return "x = ", round(x, 2)
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return "x1 = ", round(x1, 2), "x2 = ", round(x2, 2)

a = float(input("Введите коэффициент a:"))
b = float(input("Введите коэффициент b:"))
c = float(input("Введите коэффициент c:"))

roots = solve_quadratic(a, b, c)
print("Корни уравнения:", roots)