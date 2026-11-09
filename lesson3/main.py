for i in range(1, 9, 2):
    text = "input()"
    print(i, text)

print()
#
count = 0
while count <= 3:
    print("Привет")
    count += 1
print()
#

result = 0

for i in range(3):
    num = int(input())
    if num < 0:
        break
    result += num

print("Сумма всех введенных чисел", result)
print()
#
for i in range(1, 31):
    if i == 7 or i == 17 or i == 29:
        continue  # Перехожим на следующую итерацию (и не доходим до print)
    print(i)
