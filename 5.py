from functools import reduce

print(reduce(lambda a,b : a*b, [num for num in range(100, 1001, 2)]))
