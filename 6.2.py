from itertools import cycle

list = [chr(num) for num in range(97, 123)]

cnt = 0
for el in cycle(list):
    if cnt > 100:
        break

    print(el)
    cnt += 1
