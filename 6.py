from itertools import count

def validate (var):
    error = 0

    try:
        var = int(var)
    except ValueError:
        error = 1

    return error, var

start = input('начальное значение: ')
stop = input('конечное значение: ')

error, start = validate(start)
if not error:
    error, stop = validate(stop)
    if not error:
        if start <= stop:
            for el in count(start):
                if el > stop:
                    break
                else:
                    print(el)

            exit(0)

print("Ошибка валидации")
