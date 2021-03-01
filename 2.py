class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

var1 = 10
var2 = 'e'
try:
    if var2 == 0:
        raise OwnError('На ноль делить нельзя')
    var3 = var1 / var2
    print(var3)
except Exception as e:
    print(e)

print('the end')

