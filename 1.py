def func (a, b):
    if b == 0:
        print('на ноль делить нельзя!')
        return 1
    print(a / b)
    
    return 0

def validation (a, b):
    
    error = 0
    
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            error = 1
            
    return error, a, b
    
a = input('первое число ')
b = input('второе число ')

error, a, b = validation(a, b)
if error:
    print('ошибка валидации чисел')
else:
    func(a, b)

