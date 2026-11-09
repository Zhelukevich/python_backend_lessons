# Список выражений (list comprehension)

numbers = []

for i in range(6):
    numbers.append(i)

print(numbers)

# Списочные выражение
numbers = [i for i in range(6) if i % 2 == 0]
print(numbers)

word = "Hello"
numbers = [1, 14, 5, 9, 12]
words = ["one", "two", "three", "four", "five", "six"]

print([c * 2 for c in word])
print([m[0] for m in words])
print([i for i in numbers if i < 10])
print([m[0] for m in words if len(m) == 3])
