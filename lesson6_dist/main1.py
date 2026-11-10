author = {
    "name": "Pasha",
    "age": 20,
}

print(author["name"])
print(author.get("surname", "Test"))

author["age"] = 18
author["is_mentor"] = True
deleted_name = author.pop("name")

print(author, deleted_name)
