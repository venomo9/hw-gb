import random

le = 10
list = [random.randint(-le, le) for _ in range(le)]
print(list)
new_list = [list[index] for index in range(1, len(list)) if list[index] > list[index-1]]
print(new_list)
