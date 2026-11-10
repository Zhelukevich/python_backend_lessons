languages = {"python", "javascript", "c++", "c++", "c#"}
languages.remove("c++")
languages.add("java")
print(languages)


my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 6, 7, 8}

# Объединение
print(my_set1 | my_set2)
# Пересечение:
print(my_set1 & my_set2)
# Симметрическая разность
print(my_set1 ^ my_set2)
# Разность
print(my_set1 - my_set2)
print(my_set2 - my_set1)
