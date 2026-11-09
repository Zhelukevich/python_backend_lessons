language = input("Введите лучший язык программирования: ")

if language == "Python":
    print("Верно")
else:
    print("Неверно")

# and or not

age = 20
if age < 10:
    print("Доступ запрещен")
elif age > 18 and age < 99:
    print("Проходите")
elif age >= 99:
    print("Вам очень много лет")
else:
    print("Вам ровно 18 лет")
