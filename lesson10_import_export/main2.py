import datetime
import math
import random

from colorama import Fore, init

print(math.sqrt(25))

print(datetime.datetime.now())

print(random.randint(1, 20))

init(autoreset=True)


def valid_list(key, obj):
    try:
        return obj[key]
    except KeyError:
        print(Fore.RED + f"Произошла ошибка: Ключа {key} нет")


user = {"name": "Pasha", "age": 50}
valid_list("email", user)  # Выведет текст красным цветом
print(Fore.GREEN + f"Имя: {valid_list('name', user)}")  # Выведет зеленым
