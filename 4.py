def my_func (a, b):
    fin = 1
    for _ in range(b):
        fin *= a;
    return 1/fin

def validation (a, var_type):
    error = 0
    try:
        a = var_type(a)
    except ValueError:
        error = 1
            
    return error, a
    
x = input('x = ')
y = input('y = ')

error, x = validation(x, float)
if not error and x > 0:
    error, y = validation(y, int)
    if not error and y < 0:
        print(my_func(x, abs(y)))
        exit(0)

print('ошибка валидации входных данных')


    
