def get_sum(*args):  # Картеж ()
    total_sum = 0

    for num in args:
        total_sum += num

    return total_sum


print(get_sum(1, 5))


def print_info(name, *args, **kwargs):  # Словарь
    print(name, args, kwargs)


print_info(5, 1, 5, 36, country="Belarus")


def get_average(*args):
    if not args:
        return 0

    total_sum = 0

    for num in args:
        total_sum += num

    return total_sum / len(args)


print(get_average(1, 2, 3, 4))
