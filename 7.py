class Comp:
    def __init__(self, var, vari):
        self.var = var
        self.vari = vari

    def __add__(self, other):
        var  = self.var + other.var
        vari = self.vari + other.vari

        return Comp(var, vari)

    def __sub__(self, other):
        var  = self.var - other.var
        vari = self.vari - other.vari

        return Comp(var, vari)

    def info(self):
        ret = str(self.var)
        if self.vari > -1:
            ret += '+'
        ret += str(self.vari) + 'i'
        
        return ret



comp = Comp(1, -3)
print(comp.info())
