class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

list = []
while True:
    inp = input("введите число: ")
    if inp == 'stop':
        break

    error = 0

    try:
        inp = int(inp)
    except:
        error = 1

    if error:
        try:
            raise OwnError('Вы ввели не число')
        except OwnError as e:
            print(e)
    else:
        list.append(inp)

print(list)
print('the end')

