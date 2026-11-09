num = int(input("Введите положительное число"))

if (num % 2) == 0:
    print("Правильно")
elif (num % 2) == 1:
    print("Неправильно")
else:
    print("Не число")

scope = 85
match scope:
    case s if s >= 90:
        print("Оценка отличная")
    case s if s >= 75:
        print("Оценка хорошо")
    case s if s >= 60:
        print("Оценка удовлетворительно")
    case _:  # Остальные значения, которые не подошли ни в одном case
        print("Оценка отличная")
