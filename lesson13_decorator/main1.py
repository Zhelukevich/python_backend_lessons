import time


def decorator_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Время выполнения: {end - start}")

        return result

    return wrapper


@decorator_timer
def load_file(seconds: float) -> None:
    print("Загружаю какой-то файл")
    time.sleep(seconds)


load_file(2)
load_file(0.5)


@decorator_timer
def multiply(a, b):
    return a * b


print(multiply(5, 6))
