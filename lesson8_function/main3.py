birth_year = 123


def print_pasha():
    birth_year = 356
    print("Pasha the Great was born in", birth_year, "BC.")
    print(f"ЛОКАЛЬНАЯ область видимости print_pasha: {locals()}")
    print(globals())


print_pasha()
print(birth_year)
print(globals())
