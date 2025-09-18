

def calculate_bmi(weight, height):
    a = weight / (height ** 2)
    return a

def get_bmi_category(bmi):
    if bmi < 25:
        return "Норма, жить можно"
    elif 25 < bmi < 30:
        return "Избыточный вес, стоит задуматься"
    else:
        return "Ожирение"

weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м)"))

if weight < 0:
    print("Вес не может быть отрицательными")
elif height < 0:
    print("Рост не может быть отрицательными")
else:
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print("Ваш ИМТ: ", round(bmi, 1))
    print("Категория: ", category)