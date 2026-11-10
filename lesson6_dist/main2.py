author = {
    "name": "Pasha",
    "age": 28,
    "is_mentor": False,
}

user = ["Pasha", 28, False]

for key in author.keys():
    print(key)

print(list(author.keys()))


for value in author.values():
    print(value)

print(list(author.values()))


for key, value in author.items():
    print(key, value)

print(list(author.items()))
