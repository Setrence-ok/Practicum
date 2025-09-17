
def to_fahrenheit(celsius):
    far = (celsius * 9/5) + 32
    return far

def to_kelvin(celsius):
    cel = celsius + 273.15
    return cel

celsius = float(input("Введите температуру в Цельсиях: "))
print("Фаренгейт:", round(to_fahrenheit(celsius), 2))
print("Кельвин:", round(to_kelvin(celsius), 2))