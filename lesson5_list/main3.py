# number = [0, 1, 2, 3, 4, 5, 6]

# for i in number:
#     print(i)

languages = ["Python", "JavaScript", "ts", "go"]

for index, element in enumerate(languages):
    if languages[index] == "JavaScript":
        languages.insert(index + 1, "C#")
        break
    print(languages)

print(languages)
