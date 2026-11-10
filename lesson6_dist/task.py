user = {
    "name": "Pasha",
    "surname": "Zhelukevich",
    "city": "Minsk",
}


print(user["name"])
print(user.get("surname"))
user["city"] = "Grodno"
print(user)
user["learning_python"] = True
user.pop("city")

for key, value in user.items():
    print(f"{key} - {value}")
