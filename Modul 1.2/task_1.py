
def sum(number_1, number_2):
    summa = number_1 + number_2
    return summa

def difference(number_1, number_2):
    diff = number_1 - number_2
    return diff

def compositions(number_1, number_2):
    comp = number_1 * number_2
    return comp

def division(number_1, number_2):
    div = number_1 / number_2
    return div

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

print("The sum of", number_1, "and", number_2, "is", sum(number_1, number_2))
print("The difference of ", number_1, "and", number_2, "is", difference(number_1, number_2))
print("The composition of ", number_1, "and", number_2, "is", compositions(number_1, number_2))
print("The division of ", number_1, "and", number_2, "is", division(number_1, number_2))