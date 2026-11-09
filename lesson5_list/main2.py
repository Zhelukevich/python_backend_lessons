my_list = [2, 5, 99, 42, 1]
print(sum(my_list))
print(min(my_list))
print(max(my_list))

# Добавление
my_list.append(6)

my_list.insert(0, 5)
print(my_list)

# Удаление
deleted = my_list.pop(0)
print(f"my_list: {my_list} | Deleted: {deleted}")

my_list.remove(1)
print(my_list)

my_list.sort(reverse=True)
print(my_list)
