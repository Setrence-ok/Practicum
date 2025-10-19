
def calculate_months_to_threshold(start, rate, threshold):
    if start >= threshold:
        return 0
    elif rate <= 0:
        raise ValueError("Growth rate must be greater than 0.")
    elif start <= 0 or threshold <= 0:
        raise ValueError("Start and threshold must be positive numbers.")
    else:
        rate = rate / 100
        months_to_threshold = 0
        while start <= threshold:
            start = start + (start * rate)
            months_to_threshold += 1
            if months_to_threshold > 1000:
                break
        return months_to_threshold

# Пример использования
start = int(input("Введите начальное количество пользователей: "))
rate = float(input("Введите темп роста в процентах: "))
threshold = int(input("Введите пороговое значение: "))

months = calculate_months_to_threshold(start, rate, threshold)
print(f"Количество месяцев для достижения порога: {months}")