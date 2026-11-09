# 1 task

numbers = [12, 5, 8, 99, 3, 8]
print(numbers[0], numbers[-1])
print(8 in numbers)
print(min(numbers), max(numbers), sum(numbers))
print()

# 2 task
gods = ["Zeus", "Apollo", "Ares"]
gods.append("Hermes")
print(gods)

# for i, el in enumerate(gods):
#     if gods[i] == "Zeus":
#         gods.insert(i + 1, "Hades")
#         break
# print(gods)

idx = gods.index("Zeus") + 1
gods.insert(idx, "Hades")
print(gods)

gods.remove("Apollo")
print(gods)

deleted_last = gods.pop(-1)
print(deleted_last, gods)
print()

# 3 task
numbers = [4, 7, 10, 15, 18, 21, 24]

for i in numbers:
    print(i)

for i in numbers:
    if i % 2 == 0:
        print(i)
        continue

for i, el in enumerate(numbers):
    print(i, el)

result = 0
for i in numbers:
    if i > 10:
        result += 1
print(result)
print()

# 4 task
text = "Введите сообщение: "  # input()

text_list = text.split(" ")
print(text_list)
print("-".join(text_list))


# 5 task
print([i**2 for i in range(1, 11) if i % 3 != 0])
