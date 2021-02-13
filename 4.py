import random

list = [random.randint(0, 10) for _ in range(10)]
print(list)
print([l for l in list if list.count(l) == 1])

