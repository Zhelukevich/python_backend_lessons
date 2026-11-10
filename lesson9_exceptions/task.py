def valid_list(key, obj):

    if key not in obj:
        raise ValueError(f"Ключа {key} нет")
    else:
        return obj[key]


user = {"name": "Pasha", "age": 50}
print(valid_list("email", user))
print(valid_list("name", user))
