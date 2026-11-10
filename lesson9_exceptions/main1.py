# try:
#     number = int(input("Введите число: "))
#     print(10 / number)
# except ZeroDivisionError:
#     print("Не вводи 0")
# except ValueError:
#     print("Введи число")


# Обработка ошибок:
# 1) ZeroDivisionError
# 2) ValueError


try:
    number = int(input("Введите число: "))
    print(10 / number)
except Exception as error:
    print(f"Произошла ошибка {error}")
else:
    print("Ошибок нет")
finally:
    print("Этот текст будет выведен всегда")


age = int(input())
if age < 0:
    raise ValueError("Введите корректный возраст")
