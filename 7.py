def fact(n):
    ret = 1
    for el in range(1,(n+1)):
        ret *= el
        yield ret

# без валидации.
n = int(input('введите n: '))

if n < 0:
    print('факториал бывает только у положительных чисел и 0')
    exit(1)

for f in fact(n):
    print(f)
