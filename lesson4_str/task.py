# task №1
# message = input('Введите строку')
# message = message.strip()

# if len(message) == 0:
#   print('EMPTY')
# elif 'spam' in message.lower():
#   print('BLOCKED')
# else:
#   print(message)

# task №2
s = input("Введите строку: ")
i = int(input("Введите число: "))

if 0 <= i < len(s):
    char = s[i]
    is_a = char.lower() == "a"
    print(char, is_a)
else:
    print("IndexError")

# task №3
full_name = input()
full_name = full_name.strip()
full_name = full_name.capitalize()
print(full_name)


print(f"{full_name[0]}. {full_name[-1]}")
