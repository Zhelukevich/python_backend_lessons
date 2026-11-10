student = ("Pasha", 28, "Python")
name, age, language = student
print(name, age, language)

words = ["python", "code", "list", "python", "set", "code"]
set_words = set(words)
print(set_words)
print("tuple" in set_words)
set_words.remove("list")
set_words.add("loop")
print(set_words)
