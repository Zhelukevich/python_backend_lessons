def double(number):
    result = number * 2
    return result


num = 5
result = double(num)
print(result)


def check_number(number):
    if number > 0:
        return "Положительное"
    elif number < 0:
        return "Отрицательное"
    return "Ноль"


print(check_number(8))
print(check_number(-5))
print(check_number(0))


def get_square(number):
    return number**2


result = get_square(4)
print(result + 10)


def check_age(age):
    if age < 12:
        return "Ребёнок"
    elif 12 <= age <= 17:
        return "Подросток"
    elif age > 18:
        return "Взрослый"

    return


print(check_age(15))
