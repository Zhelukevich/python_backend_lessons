# 1 task ---------------------------------------
# for i in range(3, 10, 3):
#   print(i)

# print()

# 2 task ---------------------------------------
# num = int(input())
# result = 0
# for i in range(1, num + 1):
#   result += i

# if result % 2 == 0:
#   print(result)
# else:
#   print('Не четное')

# 3 task ---------------------------------------
# num = int(input())
# result = 0
# while(num != 0):
#   result +=num
#   num = int(input())

# print(result)

# 4 task ---------------------------------------
# result = 0
# for i in range(10):
#   num = int(input())

#   if num < 0:
#     break

#   result += num

# print(result)

# 5 task ---------------------------------------

for i in range(1, 31):
    if i % 3 == 0:
        continue

    print(i)
