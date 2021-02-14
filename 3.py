def my_func (a, b, c):
    if c <= a and c <= b:
        return a + b
    elif b <= a and b <= c:
        return a + c
    else:
        return b + c

def validation (a, b, c):
    error = 0
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except ValueError:
            error = 1
            
    return error, a, b, c
    
a = input('первое число ')
b = input('второе число ')
c = input('третье число ')

error, a, b, c = validation(a, b, c)
if error:
    print('ошибка валидации чисел')
else:
    print(my_func(a, b, c))
